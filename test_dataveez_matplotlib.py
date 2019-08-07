# import the required modules
import pandas as pd
from dataveez_matplotlib import*


# define the function blocks
def test_plotdata():
    dataset_df= pd.read_csv("../datasets/anscombe_df.csv")
    print(dataset_df.head())
    plotdata(dataset_df['x'], dataset_df['y'], "x_axis", "y_axis", title="plot_x_vs_y", file_path="figures/", filename="fig_xy")


def test_pltHist():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    pltHist(tips['total_bill'], "Frequency", "Total Bill", title="Histogram of Total Bill", file_path="figures/", filename="total_bill")


def test_pltScatter():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    pltScatter(tips['total_bill'], tips['tip'], "Total Bill", "Tip", title="Scatterplot of Total Bill vs Tip", file_path="figures/", filename="total_bill_vs_tip")


def test_pltBoxplot():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    female_tip = tips[tips["sex"]=="Female"]["tip"]
    male_tip = tips[tips["sex"]=="Male"]["tip"]
    pltBoxplot(female_tip, male_tip, "Sex", "Tip", label_param_1="Female", label_param_2="Male", title="Boxplot of Tips by Sex", file_path="figures/", filename="tips_by_sex")


def test_pltScatterMultivar():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())
    # Create a color variable based on the sex

    def record_sex(sex):
        if sex == 'Female':
            return 0
        else:
            return 1

    # Add a column 'sex_color' to the tips dataframe
    tips['sex_color'] = tips['sex'].apply(record_sex)
    print(tips.head())
    pltScatterMultivar(tips['total_bill'], tips['tip'], "Total Bill", "Tip", color_var=tips["sex_color"], size=tips["size"]*10, title="Total Bill vs Tip colored by sex and sized by size", file_path="figures/", filename="total_bill_vs_tip_coloredby_sex_sizedby_size")


def test_subplotMbyN():
        anscombe= pd.read_csv("../datasets/anscombe.csv")
        print(anscombe.head())
        print(anscombe.tail())

        # Create subsets of the anscombe data
        dataset_1 = anscombe[anscombe['dataset']=='I']
        dataset_2 = anscombe[anscombe['dataset']=='II']
        dataset_3 = anscombe[anscombe['dataset']=='III']
        dataset_4 = anscombe[anscombe['dataset']=='IV']

        axes1_data = [dataset_1["x"], dataset_1["y"]]
        axes2_data = [dataset_2["x"], dataset_2["y"]]
        axes3_data = [dataset_3["x"], dataset_3["y"]]
        axes4_data = [dataset_4["x"], dataset_4["y"]]

        subplot_title = ["dataset_1", "dataset_2", "dataset_3", "data_set4"]
        x_label = ["x_label1", "x_label2", "x_label3", "x_label4"]
        y_label = ["y_label1", "y_label2", "y_label3", "y_label4"]

        subplotOneByTwo(axes1_data, axes2_data, x_label, y_label, subplot_title, sup_title="Anscombe Data", file_path="figures/", filename="anscombe_subplot_1x2")
        subplotTwoByOne(axes1_data, axes2_data, x_label, y_label, subplot_title, sup_title="Anscombe Data", file_path="figures/", filename="anscombe_subplot_2x1")
        subplotThreeByOne(axes1_data, axes2_data, axes3_data, x_label, y_label, subplot_title, sup_title="Anscombe Data", file_path="figures/", filename="anscombe_subplot_3x1")
        subplotTwoByTwo(axes1_data, axes2_data, axes3_data, axes4_data, x_label, y_label, subplot_title, sup_title="Anscombe Data", file_path="figures/", filename="anscombe_subplot_2x2")


def test_subplotHistMbyN():
        anscombe= pd.read_csv("../datasets/anscombe.csv")
        print(anscombe.head())
        print(anscombe.tail())

        # Create subsets of the anscombe data
        dataset_1 = anscombe[anscombe['dataset']=='I']
        dataset_2 = anscombe[anscombe['dataset']=='II']
        dataset_3 = anscombe[anscombe['dataset']=='III']
        dataset_4 = anscombe[anscombe['dataset']=='IV']

        axes1_data = dataset_1["x"]
        axes2_data = dataset_2["x"]
        axes3_data = dataset_3["x"]
        axes4_data = dataset_4["x"]

        subplot_title = ["dataset_1", "dataset_2", "dataset_3", "dataset_4"]
        x_label = "frequency"
        y_label = ["y_label1", "y_label2", "y_label3", "y_label4"]

        subplotHistOneByTwo(axes1_data, axes2_data, x_label, y_label, subplot_title, sup_title="Anscombe Data", file_path="figures/", filename="ex_subplot_hist_1x2")
        subplotHistTwoByOne(axes1_data, axes2_data, x_label, y_label, subplot_title, sup_title="Anscombe Data", file_path="figures/", filename="ex_subplot_hist_2x1")
        subplotHistThreeByOne(axes1_data, axes2_data, axes3_data, x_label, y_label, subplot_title, sup_title="Anscombe Data", file_path="figures/", filename="ex_subplot_hist_3x1")
        subplotHistTwoByTwo(axes1_data, axes2_data, axes3_data, axes4_data, x_label, y_label, subplot_title, sup_title="Anscombe Data", file_path="figures/", filename="ex_subplot_hist_2x2")


def test_subplotScatterMbyN():
        anscombe= pd.read_csv("../datasets/anscombe.csv")
        print(anscombe.head())
        print(anscombe.tail())

        # Create subsets of the anscombe data
        dataset_1 = anscombe[anscombe['dataset']=='I']
        dataset_2 = anscombe[anscombe['dataset']=='II']
        dataset_3 = anscombe[anscombe['dataset']=='III']
        dataset_4 = anscombe[anscombe['dataset']=='IV']

        axes1_data = [dataset_1["x"], dataset_1["y"]]
        axes2_data = [dataset_2["x"], dataset_2["y"]]
        axes3_data = [dataset_3["x"], dataset_3["y"]]
        axes4_data = [dataset_4["x"], dataset_4["y"]]

        subplot_title = ["dataset_1", "dataset_2", "dataset_3", "dataset_4"]
        x_label = ["x_label1", "x_label2", "x_label3", "x_label4"]
        y_label = ["y_label1", "y_label2", "y_label3", "y_label4"]

        subplotScatterOnebyTwo(axes1_data, axes2_data, x_label, y_label, subplot_title, sup_title="Anscombe Data", file_path="figures/", filename="ex_subplot_scatter_1x2")
        subplotScatterTwoByOne(axes1_data, axes2_data, x_label, y_label, subplot_title, sup_title="Anscombe Data", file_path="figures/", filename="ex_subplot_scatter_2x1")
        subplotScatterThreeByOne(axes1_data, axes2_data, axes3_data, x_label, y_label, subplot_title, sup_title="Anscombe Data", file_path="figures/", filename="ex_subplot_scatter_3x1")
        subplotScatterTwoByTwo(axes1_data, axes2_data, axes3_data, axes4_data, x_label, y_label, subplot_title, sup_title="Anscombe Data", file_path="figures/", filename="ex_subplot_scatter_2x2")


def test_subplotBoxplotMbyN():
    tips = pd.read_csv("../datasets/tips.csv")
    print(tips.head())

    female_tip = tips[tips["sex"]=="Female"]["tip"]
    male_tip = tips[tips["sex"]=="Male"]["tip"]
    axes1_data = [female_tip, male_tip]

    female_total_bill = tips[tips["sex"]=="Female"]["total_bill"]
    male_total_bill = tips[tips["sex"]=="Male"]["total_bill"]
    axes2_data = [female_total_bill, male_total_bill]

    smoker_tip = tips[tips["smoker"]=="Yes"]["tip"]
    nonsmoker_tip = tips[tips["smoker"]=="No"]["tip"]
    axes3_data = [smoker_tip, nonsmoker_tip]

    smoker_total_bill = tips[tips["smoker"]=="Yes"]["total_bill"]
    nonsmoker_total_bill = tips[tips["smoker"]=="No"]["total_bill"]
    axes4_data = [smoker_total_bill, nonsmoker_total_bill]

    x_label = ["Sex", "Sex", "smoker", "smoker"]
    y_label = ["tip", "total_bill", "tip", "total_bill"]
    label_param = [["Female", "Male"], ["Female", "Male"], ["smoker", "nonsmoker"], ["smoker", "nonsmoker"]]
    subplot_title = ["Tips_by_sex", "Totalbill_by_sex", "Tips_by_smoker", "Totalbill_by_smoker"]

    subplotBoxplotOnebyTwo(axes1_data, axes2_data, x_label, y_label, label_param, subplot_title, sup_title="Tips Data", file_path="figures/", filename="ex_subplot_boxplot_1x2")
    subplotBoxplotTwoByOne(axes1_data, axes2_data, x_label, y_label, label_param, subplot_title, sup_title="Tips Data", file_path="figures/", filename="ex_subplot_boxplot_2x1")
    subplotBoxplotThreeByOne(axes1_data, axes2_data, axes3_data, x_label, y_label, label_param, subplot_title, sup_title="Tips Data", file_path="figures/", filename="ex_subplot_boxplot_3x1")
    subplotBoxplotTwoByTwo(axes1_data, axes2_data, axes3_data, axes4_data, x_label, y_label, label_param, subplot_title, sup_title="Tips Data", file_path="figures/", filename="ex_subplot_boxplot_2x2")

