""" Download and preprocess the Ames Housing dataset """

from pathlib import Path
import pickle
import pandas as pd
import numpy as np
import requests
from config import (
    ignore_variables,
    continuous_variables,
    discrete_variables,
    categorical_variables,
    category_orderings,
    lis_features,
)

MAIN_DIR = Path.cwd()
DATA_DIR = MAIN_DIR / "data"
FEAST_DATA_DIR = MAIN_DIR / "feast" / "experiment" / "feature_repo" / "data"
URL = "https://www.openintro.org/book/statdata/ames.csv"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/39.0.2171.95 Safari/537.36",
}


def download_data():
    """Download the Ames Housing dataset"""
    response = requests.get(URL, headers=HEADERS, timeout=5)
    csv_content = response.content.decode("utf-8")
    with open(DATA_DIR / "ames.csv", "w", encoding="utf-8") as file:
        file.write(csv_content)


def drop_ingored_variables(df):
    """Drop the variables to be ignored"""
    df.drop(columns=ignore_variables, inplace=True)
    return df


def convert_types(df):
    """Convert the types of variables"""
    df[continuous_variables] = df[continuous_variables].astype("float64")
    df[discrete_variables] = df[discrete_variables].astype("float64")
    df[categorical_variables] = df[categorical_variables].astype("category")
    for col, ordering in category_orderings.items():
        df[col] = df[col].astype("category").cat.set_categories(ordering, ordered=True)
    return df


def concat_ms_zoning(df):
    """Concatenate the MS.Zoning variable and remove unused categories"""
    selection = ~(df["MS.Zoning"].isin(["A (agr)", "C (all)", "I (all)"]))
    df = df.loc[selection].copy()
    df["MS.Zoning"] = df["MS.Zoning"].cat.remove_unused_categories()
    return df


def remap_categories(
    series: pd.Series,
    old_categories: tuple[str],
    new_category: str,
) -> pd.Series:
    """Remap categories in a pandas Series"""
    series = series.cat.add_categories(new_category)
    remapped_items = series.isin(old_categories)
    series.loc[remapped_items] = new_category
    series = series.cat.remove_unused_categories()
    return series


def drop_street_column(df):
    """Drop the Street column"""
    df.drop(columns="Street", inplace=True)
    return df


def remap_conditions(df):
    """Remap the Condition.1 and Condition.2 variables"""
    for col in ("Condition.1", "Condition.2"):
        df[col] = remap_categories(
            series=df[col],
            old_categories=("RRAn", "RRAe", "RRNn", "RRNe"),
            new_category="Railroad",
        )
        df[col] = remap_categories(
            series=df[col],
            old_categories=("Feedr", "Artery"),
            new_category="Roads",
        )
        df[col] = remap_categories(
            series=df[col],
            old_categories=("PosA", "PosN"),
            new_category="Positive",
        )
    return df


def combine_conditions(df):
    """Combine the Condition.1 and Condition.2 variables"""
    df["Condition"] = pd.Series(
        index=df.index,
        dtype=pd.CategoricalDtype(
            categories=(
                "Norm",
                "Railroad",
                "Roads",
                "Positive",
                "RoadsAndRailroad",
            )
        ),
    )

    norm_items = df["Condition.1"] == "Norm"
    df.loc[norm_items, "Condition"] = "Norm"

    railroad_items = (df["Condition.1"] == "Railroad") & (df["Condition.2"] == "Norm")
    df.loc[railroad_items, "Condition"] = "Railroad"

    roads_items = (df["Condition.1"] == "Roads") & (df["Condition.2"] != "Railroad")
    df.loc[roads_items, "Condition"] = "Roads"

    positive_items = df["Condition.1"] == "Positive"
    df.loc[positive_items, "Condition"] = "Positive"

    roads_and_railroad_items = (
        (df["Condition.1"] == "Railroad") & (df["Condition.2"] == "Roads")
    ) | ((df["Condition.1"] == "Roads") & (df["Condition.2"] == "Railroad"))
    df.loc[roads_and_railroad_items, "Condition"] = "RoadsAndRailroad"
    df = df.drop(columns=["Condition.1", "Condition.2"])
    return df


def misc_feature_to_has_shed(df):
    """Convert the Misc.Feature variable to a binary variable Has.Shed"""
    df["HasShed"] = df["Misc.Feature"] == "Shed"
    df.drop(columns="Misc.Feature", inplace=True)
    return df


def alley_to_has_alley(df):
    """Convert the Alley variable to a binary variable Has.Alley"""
    df["HasAlley"] = df["Alley"].notna()
    df.drop(columns="Alley", inplace=True)
    return df


def fix_exterior_1st_2nd(df):
    """Fix the Exterior.1st and Exterior.2nd variables"""
    df["Exterior.2nd"] = remap_categories(
        series=df["Exterior.2nd"],
        old_categories=("Brk Cmn",),
        new_category="BrkComm",
    )
    df["Exterior.2nd"] = remap_categories(
        series=df["Exterior.2nd"],
        old_categories=("CmentBd",),
        new_category="CemntBd",
    )
    df["Exterior.2nd"] = remap_categories(
        series=df["Exterior.2nd"],
        old_categories=("Wd Shng",),
        new_category="WdShing",
    )
    for col in ("Exterior.1st", "Exterior.2nd"):
        categories = df[col].cat.categories
        df[col] = df[col].cat.reorder_categories(sorted(categories))

    mat_count = df["Exterior.1st"].value_counts()
    rare_materials = list(mat_count[mat_count < 40].index)
    df["Exterior"] = remap_categories(
        series=df["Exterior.1st"],
        old_categories=rare_materials,
        new_category="Other",
    )
    df = df.drop(columns=["Exterior.1st", "Exterior.2nd"])
    return df


def drop_heat(df):
    """Drop the Heating variable"""
    df.drop(columns=["Heating"], inplace=True)
    return df


def drop_roof_matl(df):
    """Drop the Roof.Matl variable"""
    df.drop(columns=["Roof.Matl"], inplace=True)
    return df


def group_roof_style(df):
    """Group the Roof.Style variable"""
    df["Roof.Style"] = remap_categories(
        series=df["Roof.Style"],
        old_categories=[
            "Flat",
            "Gambrel",
            "Mansard",
            "Shed",
        ],
        new_category="Other",
    )
    return df


def fiz_and_transform_mas_vnr_type(df):
    """Fix and transform the Mas.Vnr.Type variable"""
    df["Mas.Vnr.Type"] = remap_categories(
        series=df["Mas.Vnr.Type"],
        old_categories=[
            "BrkCmn",
            "CBlock",
        ],
        new_category="Other",
    )
    df["Mas.Vnr.Type"] = df["Mas.Vnr.Type"].astype("category")
    df["Mas.Vnr.Type"] = df["Mas.Vnr.Type"].cat.add_categories("None")
    df.loc[df["Mas.Vnr.Type"].isna(), "Mas.Vnr.Type"] = "None"
    return df


def remap_ms_subclass(df):
    """Remap the MS.SubClass variable"""
    df["MS.SubClass"] = remap_categories(
        series=df["MS.SubClass"],
        old_categories=[75, 45, 180, 40, 150],
        new_category="Other",
    )
    return df


def remap_foundation(df):
    """Remap the Foundation variable"""
    df["Foundation"] = remap_categories(
        series=df["Foundation"],
        old_categories=["Slab", "Stone", "Wood"],
        new_category="Other",
    )
    return df


def transform_neighborhood(df):
    """Transform the Neighborhood variable"""
    selection = ~df["Neighborhood"].isin(
        [
            "Blueste",
            "Greens",
            "GrnHill",
            "Landmrk",
        ]
    )
    df = df.loc[selection].copy()
    df["Neighborhood"] = df["Neighborhood"].cat.remove_unused_categories()
    return df


def transform_garage(df):
    """Transform the Garage.Type variable"""
    df["Garage.Type"] = df["Garage.Type"].cat.add_categories(["NoGarage"])
    df.loc[df["Garage.Type"].isna(), "Garage.Type"] = "NoGarage"
    return df


def drop_utilities(df):
    """Drop the Utilities variable"""
    df.drop(columns=["Utilities"], inplace=True)
    return df


def drop_pool(df):
    """Drop the Pool.QC variable"""
    df.drop(columns=["Pool.QC"], inplace=True)
    return df


def transform_fence(df):
    """Transform the Fence variable"""
    old_categories = list(df["Fence"].cat.categories)
    new_categories = old_categories + ["NoFence"]
    df["Fence"] = df["Fence"].cat.set_categories(new_categories)
    df.loc[df["Fence"].isna(), "Fence"] = "NoFence"

    return df


def drop_fireplace(df):
    """Drop the Fireplace.Qu variable"""
    df.drop(columns=["Fireplace.Qu"], inplace=True)
    return df


def drop_garage_cond_qual(df):
    """Drop the Garage.Cond and Garage.Qual variables"""
    df.drop(columns=["Garage.Cond", "Garage.Qual"], inplace=True)
    return df


def transform_garage_finish(df):
    """Transform the Garage.Finish variable"""
    df["Garage.Finish"] = (
        df["Garage.Finish"].cat.as_unordered().cat.add_categories(["NoGarage"])
    )
    df.loc[df["Garage.Finish"].isna(), "Garage.Finish"] = "NoGarage"
    return df


def fill_missing_eletcrical(df):
    """fill the mising values with Sbrk"""
    df["Electrical"] = df["Electrical"].fillna("SBrkr")
    return df


def transform_bsmt(df):
    """Transform the Basement variables"""
    df.loc[df["Bsmt.Exposure"].isna(), "Bsmt.Exposure"] = "NA"
    df["Bsmt.Exposure"] = (
        df["Bsmt.Exposure"].cat.as_unordered().cat.remove_unused_categories()
    )

    for col in ("Bsmt.Qual", "Bsmt.Cond", "BsmtFin.Type.1", "BsmtFin.Type.2"):
        df[col] = df[col].cat.add_categories(["NA"])
        df.loc[df[col].isna(), col] = "NA"
        df[col] = df[col].cat.as_unordered().cat.remove_unused_categories()
    df.loc[df["Bsmt.Cond"] == "Po", "Bsmt.Cond"] = "Fa"
    df.loc[df["Bsmt.Cond"] == "Ex", "Bsmt.Cond"] = "Gd"
    df["Bsmt.Cond"] = df["Bsmt.Cond"].cat.remove_unused_categories()
    return df


def transform_lot_frontage(df):
    """Transform the Lot.Frontage variable"""
    df["Lot.Frontage"] = df["Lot.Frontage"].fillna(df["Lot.Frontage"].median())
    return df


def remape_sales_price(df):
    """Remap the SalePrice variable"""
    df["SalePrice"] = df["SalePrice"].apply(np.log10)
    return df


def remape_garage_year(df):
    """Remap the Garage.Year.Built variable"""
    garage_age = df["Yr.Sold"] - df["Garage.Yr.Blt"]
    garage_age[garage_age < 0.0] = 0.0
    df = df.drop(columns="Garage.Yr.Blt")
    df["Garage.Age"] = garage_age
    df["Garage.Age"] = df["Garage.Age"].fillna(df["Garage.Age"].median())
    return df


def remape_year_remod_add_built(df):
    """Remap the Year.Built and Year.Remod.Add variables"""
    remod_age = df["Yr.Sold"] - df["Year.Remod.Add"]
    remod_age[remod_age < 0.0] = 0.0
    house_age = df["Yr.Sold"] - df["Year.Built"]
    house_age[house_age < 0.0] = 0.0
    df = df.drop(columns=["Year.Remod.Add", "Year.Built"])
    df["Remod.Age"] = remod_age
    df["House.Age"] = house_age
    return df


def remape_mas_vnr_area(df):
    """Remap the Mas.Vnr.Area variable"""
    df.loc[df["Mas.Vnr.Area"].isna(), "Mas.Vnr.Area"] = 0.0


def drop_rows_with_missing_values(df):
    """Drop rows with missing values"""
    df = df.dropna(axis=0)
    return df


def remove_unused_categories(df):
    """Remove unused categories from the categorical variables"""
    for col in df.select_dtypes("category").columns:
        df[col] = df[col].cat.remove_unused_categories()
    return df


def transform_lot_area(df):
    """Transform the Lot.Area variable"""
    df["Lot.Area"] = df["Lot.Area"].apply(np.log10)
    return df


def tranform_mas_vnr_area(df):
    """Transform the Mas.Vnr.Area variable"""
    df["Mas.Vnr.Area"] = df["Mas.Vnr.Area"].replace(0, np.nan)
    df["Mas.Vnr.Area"] = np.log(df["Mas.Vnr.Area"])
    df = df[df["Mas.Vnr.Area"] > 0]

    return df


def tranform_pool_area(df):
    """covert pool area to categorical variable"""
    df["Pool.Area"] = df["Pool.Area"].apply(lambda x: 1 if x > 0 else 0)
    df["Pool.Area"] = df["Pool.Area"].astype("category")
    return df


def transform_screen_porch(df):
    """coverts screen porch to categorical variable"""
    df["Screen.Porch"] = df["Screen.Porch"].apply(lambda x: 1 if x > 0 else 0)
    df["Screen.Porch"] = df["Screen.Porch"].astype("category")
    return df


def transform_x3ssn_porch(df):
    """coverts 3 season porch to categorical variable"""
    df["X3Ssn.Porch"] = df["X3Ssn.Porch"].apply(lambda x: 1 if x > 0 else 0)
    df["X3Ssn.Porch"] = df["X3Ssn.Porch"].astype("category")
    return df


def transform_enclosed_porch(df):
    """coverts enclosed porch to categorical variable"""
    df["Enclosed.Porch"] = df["Enclosed.Porch"].apply(lambda x: 1 if x > 0 else 0)
    df["Enclosed.Porch"] = df["Enclosed.Porch"].astype("category")
    return df


def tranform_misc_val(df):
    """coverts misc val to categorical variable"""
    df["Misc.Val"] = df["Misc.Val"].apply(lambda x: 1 if x > 0 else 0)
    df["Misc.Val"] = df["Misc.Val"].astype("category")
    return df


def df_to_dummies(df):
    """Convert the categorical variables to dummy variables"""
    model_data = df.copy()
    categorical_columns = []
    ordinal_columns = []
    for col in model_data.select_dtypes("category").columns:
        if model_data[col].cat.ordered:
            ordinal_columns.append(col)
        else:
            categorical_columns.append(col)
    for col in ordinal_columns:
        codes, _ = pd.factorize(df[col], sort=True)
        model_data[col] = codes
    model_data = pd.get_dummies(model_data, drop_first=True)
    return model_data


def filter_top_15_features(df):
    """Filter the top 15 features"""
    # filter the top 15 features
    df = df[lis_features]
    return df


def save_data(df):
    """Save the preprocessed data"""
    with open(DATA_DIR / "ames_processed.pkl", "wb") as file:
        pickle.dump(df, file)
    # save in parquet format to use on feast
    df.to_parquet(FEAST_DATA_DIR / "ames_processed.parquet")


def main():
    """Main function, call all the necessary functions"""
    DATA_DIR.mkdir(exist_ok=True)
    download_data()
    df = pd.read_csv(DATA_DIR / "ames.csv")
    df = drop_ingored_variables(df)
    df = convert_types(df)
    df = concat_ms_zoning(df)
    df["Sale.Type"] = remap_categories(
        series=df["Sale.Type"],
        old_categories=("WD ", "CWD", "VWD"),
        new_category="GroupedWD",
    )
    df["Sale.Type"] = remap_categories(
        series=df["Sale.Type"],
        old_categories=("COD", "ConLI", "Con", "ConLD", "Oth", "ConLw"),
        new_category="Other",
    )
    df = drop_street_column(df)
    df = remap_conditions(df)
    df = combine_conditions(df)
    df = misc_feature_to_has_shed(df)
    df = alley_to_has_alley(df)
    df = fix_exterior_1st_2nd(df)
    df = drop_heat(df)
    df = drop_roof_matl(df)
    df = group_roof_style(df)
    df = fiz_and_transform_mas_vnr_type(df)
    df = remap_ms_subclass(df)
    df = remap_foundation(df)
    df = transform_neighborhood(df)
    df = transform_garage(df)
    df = drop_utilities(df)
    df = drop_pool(df)
    df = transform_fence(df)
    df = drop_fireplace(df)
    df = drop_garage_cond_qual(df)
    df = transform_garage_finish(df)
    df = fill_missing_eletcrical(df)
    df = transform_bsmt(df)
    df = remape_sales_price(df)
    df = transform_lot_frontage(df)
    df = remape_garage_year(df)
    df = remape_year_remod_add_built(df)
    remape_mas_vnr_area(df)
    df = drop_rows_with_missing_values(df)
    df = remove_unused_categories(df)
    df = transform_lot_area(df)
    df = tranform_mas_vnr_area(df)
    df = tranform_pool_area(df)
    df = transform_screen_porch(df)
    df = transform_x3ssn_porch(df)
    df = transform_enclosed_porch(df)
    df = tranform_misc_val(df)
    df = df_to_dummies(df)
    df = filter_top_15_features(df)
    save_data(df)


if __name__ == "__main__":
    main()
