import pandas as pd
from dataveez_seaborn import*


def test_snsHistDensity():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    snsHistDensity(tips['total_bill'], "Total Bill", title="Total Bill Histogram with Density", file_path="figure-seaborn/", filename="total_bill_hist_with_density")


def test_plotHist():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    plotHist(tips['total_bill'], "Total Bill", "Frequency", title="Total Bill Histogram", file_path="figure-seaborn/", filename="total_bill_hist")


def test_plotDensity():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    plotDensity(tips['total_bill'], "Total Bill", "Unit Probability", title="Total Bill Density", file_path="figure-seaborn/", filename="total_bill_density")


def test_HistDenRug():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    HistDenRug(tips['total_bill'], "Total Bill", title="Total Bill Histogram with Density and Rug", file_path="figure-seaborn/", filename="total_bill_hist_density_rug")


def test_plotCount():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    plotCount(tips['day'], tips, "Day of the Week", "Frequency", title="Count of Days", file_path="figure-seaborn/", filename="count_of_days")


def test_plotScatter():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    plotScatter(tips['total_bill'], tips['tip'], tips, "Total Bill", "Tip", title="Scatter plot of Total Bill and Tip", file_path="figure-seaborn/", filename="scatterplot_totalbill_tip")


def test_scatterlmplot():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    scatterlmplot("total_bill", "tip", tips, "Total Bill", "Tip", title="Scatter plot of total bill and tips using lmplot", file_path="figure-seaborn/", filename="scatterlmplot_totalbill_tip")


def test_scatterJointplot():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    scatterJointplot(tips['total_bill'], tips['tip'], tips, "Total Bill", "Tip", title="Joint plot of Total Bill and Tip", file_path="figure-seaborn/", filename="jointplot_totalbill_tip")


def test_plotHexbin():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    plotHexbin(tips['total_bill'], tips['tip'], tips, "Total Bill", "Tip", title="Hexbin plot of Total Bill and Tip", file_path="figure-seaborn/", filename="hexbinplot_totalbill_tip")


def test_twoDimDensity():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    twoDimDensity(tips['total_bill'], tips['tip'], "Total Bill", "Tip", title="2D Density plot of Total Bill and Tip", file_path="figure-seaborn/", filename="kde_2d_totalbill_tip")


def test_denJointplot():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    denJointplot(tips['total_bill'], tips['tip'], tips, "Total Bill", "Tip", title="Kde_Joint plot of Total Bill and Tip", file_path="figure-seaborn/", filename="kde_joint_totalbill_tip")


def test_plotBar():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    plotBar(tips['time'], tips['total_bill'], tips, "Total Bill", "Tip", title="Barplot of average total bill for time of day", file_path="figure-seaborn/", filename="barplot_totalbill_for_day")


def test_plotBox():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    plotBox(tips['time'], tips['total_bill'], tips, "Total Bill", "Tip", title="Box plot of total bill by time of day", file_path="figure-seaborn/", filename="boxplot_totalbill_by_time")


def test_plotViolin():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    plotViolin(tips['time'], tips['total_bill'], tips, "Time", "Total Bill", title="Violin plot of total bill by time of day", file_path="figure-seaborn/", filename="Violinplot_totalbill_by_time")


def test_plotPair():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    plotPair(tips, title= "Pairplot of tips", file_path="figure-seaborn/", filename="pairwiseplot_tips_using_pairplot")


def test_plotPairGrid():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    plotPairGrid(tips, file_path="figure-seaborn/", filename="pairwiseplot_tips_using_pairgrid")


def test_violinMultivar():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    violinMultivar(tips['time'], tips['total_bill'], tips["sex"], tips, "Time", "Total Bill", title="Violin plot of total bill by time of day", file_path="figure-seaborn/", filename="violinplot_totalbill_by_time_multivar_using_color")


def test_scatterlmplotMultivar():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    scatterlmplotMultivar("total_bill", "tip", "sex", tips, "Total Bill", "Tip", title="lmplot of total bill and tips by sex", file_path="figure-seaborn/", filename="scatter_totalbill_by_sex_using_color")


def test_pairplotMultivar():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    pairplotMultivar(tips, "sex", title="Pairplot of tips with hue parameter", file_path="figure-seaborn/", filename="pairplot_tips_multivar")


def test_lmplotMultivar():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    lmplotMultivar("total_bill", "tip", "sex", tips, "Total Bill", "Tip", title="lmplot of total bill and tips by size and shape", file_path="figure-seaborn/", filename="lmplot_totalbill_tip_by_size_shape")


def test_lmplotFacet():
        anscombe= pd.read_csv("../datasets/anscombe.csv")
        print(anscombe.head())
        print(anscombe.tail())
        lmplotFacet('x', 'y', 'dataset', anscombe, file_path="figure-seaborn/", filename="anscombe_facet")


def test_facetGridHist():
        tips = pd.read_csv("../datasets/tips.csv")
        print(tips.head())
        facetGridHist("total_bill", tips, col_var="time", file_path="figure-seaborn/", filename="tips_facetgrid")


def test_facetGridScatter():
        tips = pd.read_csv("../datasets/tips.csv")
        print(tips.head())
        facetGridScatter("total_bill", "tip", tips, "day", "sex", file_path="figure-seaborn/", filename="tips_facetgrid_scatter")


def test_plotFacetGrid():
        tips = pd.read_csv("../datasets/tips.csv")
        print(tips.head())
        plotFacetGrid("total_bill", "tip", tips, "time", "smoker", "sex", file_path="figure-seaborn/", filename="tips_facet_grid")
