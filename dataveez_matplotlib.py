import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})


# Plot graph for dataset containing 2 continuous variables
def plotdata(x, y, x_label, y_label, title, file_path, filename):
    """This takes a vector for the x-values, and a
    corresponding vector for y-values and plots a graph
    """
    plt.plot(x, y)
    fig1 = plt.gcf()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    fig1.savefig(file_path + filename + ".png")


# Create subplots in a single figure
# ============================================
# Create 1x2 subplot
def subplotOneByTwo(axes1_data, axes2_data, x_label, y_label, subplot_title, sup_title, file_path, filename):
    """This takes two datasets each containing a vector for the x-values, and a
    corresponding vector for y-values and plots corresponding graphs
    """
    # create the figure where our subplots will go
    fig = plt.figure()
    # tell the figure how the subplots should be laid out
    # in the example below we will have, 1 row of plots, and 2 columns
    # subplot has 1 row and 2 columns, plot location 1
    axes1 = fig.add_subplot(1, 2, 1)
    axes1.plot(axes1_data[0], axes1_data[1], 'o')
    axes1.set_title(subplot_title[0])
    axes1.set_xlabel(x_label[0])
    axes1.set_ylabel(y_label[0])

    # subplot has 1 rows and 2 columns, plot location 2
    axes2 = fig.add_subplot(1, 2, 2)
    axes2.plot(axes2_data[0], axes1_data[1], 'o')
    axes2.set_title(subplot_title[1])
    axes2.set_xlabel(x_label[1])
    axes2.set_ylabel(y_label[1])

    # add a title for the entire figure
    fig.suptitle(sup_title)
    fig.savefig(file_path + filename + ".png")


# Create 2x1 subplot
def subplotTwoByOne(axes1_data, axes2_data, x_label, y_label, subplot_title, sup_title, file_path, filename):
    """This takes two datasets each containing a vector for the x-values, and a
    corresponding vector for y-values and plots corresponding graphs
    """
    # create the figure where our subplots will go
    fig = plt.figure()
    # tell the figure how the subplots should be laid out
    # in the example below we will have, 2 row of plots, each row will have 1 plot
    # subplot has 2 rows and 1 columns, plot location 1
    axes1 = fig.add_subplot(2, 1, 1)
    axes1.plot(axes1_data[0], axes1_data[1], 'o')
    axes1.set_title(subplot_title[0])
    axes1.set_xlabel(x_label[0])
    axes1.set_ylabel(y_label[0])

    # subplot has 2 rows and 1 columns, plot location 2
    axes2 = fig.add_subplot(2, 1, 2)
    axes2.plot(axes2_data[0], axes1_data[1], 'o')
    axes2.set_title(subplot_title[1])
    axes2.set_xlabel(x_label[1])
    axes2.set_ylabel(y_label[1])

    # add a title for the entire figure
    fig.suptitle(sup_title)
    fig.savefig(file_path + filename + ".png")


# Create 3x1 subplot
def subplotThreeByOne(axes1_data, axes2_data, axes3_data, x_label, y_label, subplot_title, sup_title, file_path, filename):
    """This takes 3 datasets each containing a vector for the x-values, and a
    corresponding vector for y-values and plots corresponding graphs
    """
    # create the figure where our subplots will go
    fig = plt.figure()
    # tell the figure how the subplots should be laid out
    # in the example below we will have, 3 row of plots, each row will have 1 plot
    # subplot has 3 rows and 1 column, plot location 1
    axes1 = fig.add_subplot(3, 1, 1)
    axes1.plot(axes1_data[0], axes1_data[1], 'o')
    axes1.set_title(subplot_title[0])
    axes1.set_xlabel(x_label[0])
    axes1.set_ylabel(y_label[0])

    # subplot has 3 rows and 1 columns, plot location 2
    axes2 = fig.add_subplot(3, 1, 2)
    axes2.plot(axes2_data[0], axes1_data[1], 'o')
    axes2.set_title(subplot_title[1])
    axes2.set_xlabel(x_label[1])
    axes2.set_ylabel(y_label[1])

    # subplot has 3 rows and 1 columns, plot location 3
    axes3 = fig.add_subplot(3, 1, 3)
    axes3.plot(axes3_data[0], axes1_data[1], 'o')
    axes3.set_title(subplot_title[2])
    axes3.set_xlabel(x_label[2])
    axes3.set_ylabel(y_label[2])

    # add a title for the entire figure
    fig.suptitle(sup_title)
    fig.savefig(file_path + filename + ".png")


# Create 2x2 subplot
def subplotTwoByTwo(axes1_data, axes2_data, axes3_data, axes4_data, x_label, y_label, subplot_title, sup_title, file_path, filename):
    """This takes 4 datasets each containing a vector for the x-values, and a
    corresponding vector for y-values and plots corresponding graphs
    """
    # create the figure where our subplots will go
    fig = plt.figure()
    # tell the figure how the subplots should be laid out
    # in the example below we will have, 2 row of plots, each row will have 2 plots
    # subplot has 2 rows and 2 columns, plot location 1
    axes1 = fig.add_subplot(2, 2, 1)
    axes1.plot(axes1_data[0], axes1_data[1], 'o')
    axes1.set_title(subplot_title[0])
    axes1.set_xlabel(x_label[0])
    axes1.set_ylabel(y_label[0])

    # subplot has 2 rows and 2 columns, plot location 2
    axes2 = fig.add_subplot(2, 2, 2)
    axes2.plot(axes2_data[0], axes1_data[1], 'o')
    axes2.set_title(subplot_title[1])
    axes2.set_xlabel(x_label[1])
    axes2.set_ylabel(y_label[1])

    # subplot has 2 rows and 2 columns, plot location 3
    axes3 = fig.add_subplot(2, 2, 3)
    axes3.plot(axes3_data[0], axes1_data[1], 'o')
    axes3.set_title(subplot_title[2])
    axes3.set_xlabel(x_label[2])
    axes3.set_ylabel(y_label[2])

    # subplot has 2 rows and 2 columns, plot location 4
    axes4 = fig.add_subplot(2, 2, 4)
    axes4.plot(axes4_data[0], axes1_data[1], 'o')
    axes4.set_title(subplot_title[3])
    axes4.set_xlabel(x_label[3])
    axes4.set_ylabel(y_label[3])

    # add a title for the entire figure
    fig.suptitle(sup_title)
    fig.savefig(file_path + filename + ".png")


# Statistical Graphics using matplotlib
# ======================================
# Univariate: Histograms are the most common means of looking at a single variable
# ================================================================================
def pltHist(data, x_label, y_label, title, file_path, filename):
    """This plots distribution of the variable"""
    fig = plt.figure()
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.hist(data, bins=10)
    axes1.set_title(title)
    axes1.set_xlabel(x_label)
    axes1.set_ylabel(y_label)
    fig.savefig(file_path + filename + ".png")


# Create 1x2 subplot_hist
def subplotHistOneByTwo(data1, data2,  x_label, y_label, subplot_title, sup_title, file_path, filename):
    """This plots distribution of the variable"""
    # create the figure where our subplots will go
    fig = plt.figure()
    axes1 = fig.add_subplot(1, 2, 1)
    axes1.hist(data1, bins=10)
    axes1.set_title(subplot_title[0])
    axes1.set_xlabel(x_label[0])
    axes1.set_ylabel(y_label[0])

    # subplot has 1 rows and 2 columns, plot location 2
    axes2 = fig.add_subplot(1, 2, 2)
    axes2.hist(data2, bins=10)
    axes2.set_title(subplot_title[1])
    axes2.set_xlabel(x_label[1])
    axes2.set_ylabel(y_label[1])

    # add a title for the entire figure
    fig.suptitle(sup_title)
    fig.savefig(file_path + filename + ".png")


# Create 2x1 subplot_hist
def subplotHistTwoByOne(data1, data2, x_label, y_label, subplot_title, sup_title, file_path, filename):
    """This plots distribution of the variable"""
    # create the figure where our subplots will go
    fig = plt.figure()
    axes1 = fig.add_subplot(2, 1, 1)
    axes1.hist(data1, bins=10)
    axes1.set_title(subplot_title[0])
    axes1.set_xlabel(x_label[0])
    axes1.set_ylabel(y_label[0])

    # subplot has 2 rows and 1 columns, plot location 2
    axes2 = fig.add_subplot(2, 1, 2)
    axes2.hist(data2, bins=10)
    axes2.set_title(subplot_title[1])
    axes2.set_xlabel(x_label[1])
    axes2.set_ylabel(y_label[1])

    # add a title for the entire figure
    fig.suptitle(sup_title)
    fig.savefig(file_path + filename + ".png")


# Create 3x1 subplot_hist
def subplotHistThreeByOne(data1, data2, data3, x_label, y_label, subplot_title, sup_title, file_path, filename):
    """This plots distribution of the variable"""
    # create the figure where our subplots will go
    fig = plt.figure()
    axes1 = fig.add_subplot(3, 1, 1)
    axes1.hist(data1, bins=10)
    axes1.set_title(subplot_title[0])
    axes1.set_xlabel(x_label[0])
    axes1.set_ylabel(y_label[0])

    # subplot has 3 rows and 1 columns, plot location 2
    axes2 = fig.add_subplot(3, 1, 2)
    axes2.hist(data2, bins=10)
    axes2.set_title(subplot_title[1])
    axes2.set_xlabel(x_label[1])
    axes2.set_ylabel(y_label[1])

    # subplot has 3 rows and 1 columns, plot location 3
    axes3 = fig.add_subplot(3, 1, 3)
    axes3.hist(data3, bins=10)
    axes3.set_title(subplot_title[2])
    axes3.set_xlabel(x_label[2])
    axes3.set_ylabel(y_label[2])

    # add a title for the entire figure
    fig.suptitle(sup_title)
    fig.savefig(file_path + filename + ".png")


# Create 2x2 subplot_hist
def subplotHistTwoByTwo(data1, data2, data3, data4, x_label, y_label, subplot_title, sup_title, file_path, filename):
    """This plots distribution of the variable"""
    # create the figure where our subplots will go
    fig = plt.figure()
    axes1 = fig.add_subplot(2, 2, 1)
    axes1.hist(data1, bins=10)
    axes1.set_title(subplot_title[0])
    axes1.set_xlabel(x_label[0])
    axes1.set_ylabel(y_label[0])

    # subplot has 2 rows and 2 columns, plot location 2
    axes2 = fig.add_subplot(2, 2, 2)
    axes2.hist(data2, bins=10)
    axes2.set_title(subplot_title[1])
    axes2.set_xlabel(x_label[1])
    axes2.set_ylabel(y_label[1])

    # subplot has 2 rows and 2 columns, plot location 3
    axes3 = fig.add_subplot(2, 2, 3)
    axes3.hist(data3, bins=10)
    axes3.set_title(subplot_title[2])
    axes3.set_xlabel(x_label[2])
    axes3.set_ylabel(y_label[2])

    # subplot has 2 rows and 2 columns, plot location 4
    axes4 = fig.add_subplot(2, 2, 4)
    axes4.hist(data4, bins=10)
    axes4.set_title(subplot_title[3])
    axes4.set_xlabel(x_label[3])
    axes4.set_ylabel(y_label[3])

    # add a title for the entire figure
    fig.suptitle(sup_title)
    fig.savefig(file_path + filename + ".png")


# Bivariate : refers to two variables
# ================================================================================================
# Scatter plots are used when a continuous variable is plotted against another continuous variable
def pltScatter(x, y, x_label, y_label, title, file_path, filename):
    """This plots graph of a continuous variable
    against another continuous variable
    """
    scatter_plot = plt.figure()
    axes1 = scatter_plot.add_subplot(1, 1, 1)
    axes1.scatter(x, y)
    axes1.set_title(title)
    axes1.set_xlabel(x_label)
    axes1.set_ylabel(y_label)
    scatter_plot.savefig(file_path + filename + ".png")


# Create 1x2 subplot_scatter
def subplotScatterOnebyTwo(axes1_data, axes2_data, x_label, y_label, subplot_title, sup_title, file_path, filename):
    """This plots distribution of the variable"""
    # create the figure where our subplots will go
    scatter_plot = plt.figure()
    axes1 = scatter_plot.add_subplot(1, 2, 1)
    axes1.scatter(axes1_data[0], axes1_data[1])
    axes1.set_title(subplot_title[0])
    axes1.set_xlabel(x_label[0])
    axes1.set_ylabel(y_label[0])

    # subplot has 1 rows and 2 columns, plot location 2
    axes2 = scatter_plot.add_subplot(1, 2, 2)
    axes2.scatter(axes2_data[0], axes2_data[1])
    axes2.set_title(subplot_title[1])
    axes2.set_xlabel(x_label[1])
    axes2.set_ylabel(y_label[1])

    # add a title for the entire figure
    scatter_plot.suptitle(sup_title)
    scatter_plot.savefig(file_path + filename + ".png")


# Create 2x1 subplot_scatter
def subplotScatterTwoByOne(axes1_data, axes2_data, x_label, y_label, subplot_title, sup_title, file_path, filename):
    """This plots distribution of the variable"""
    # create the figure where our subplots will go
    scatter_plot = plt.figure()
    axes1 = scatter_plot.add_subplot(2, 1, 1)
    axes1.scatter(axes1_data[0], axes1_data[1])
    axes1.set_title(subplot_title[0])
    axes1.set_xlabel(x_label[0])
    axes1.set_ylabel(y_label[0])

    # subplot has 2 rows and 1 columns, plot location 2
    axes2 = scatter_plot.add_subplot(2, 1, 2)
    axes2.scatter(axes2_data[0], axes2_data[1])
    axes2.set_title(subplot_title[1])
    axes2.set_xlabel(x_label[1])
    axes2.set_ylabel(y_label[1])

    # add a title for the entire figure
    scatter_plot.suptitle(sup_title)
    scatter_plot.savefig(file_path + filename + ".png")


# Create 3x1 subplot_scatter
def subplotScatterThreeByOne(axes1_data, axes2_data, axes3_data, x_label, y_label, subplot_title, sup_title, file_path, filename):
    """This plots distribution of the variable"""
    # create the figure where our subplots will go
    scatter_plot = plt.figure()
    axes1 = scatter_plot.add_subplot(3, 1, 1)
    axes1.scatter(axes1_data[0], axes1_data[1])
    axes1.set_title(subplot_title[0])
    axes1.set_xlabel(x_label[0])
    axes1.set_ylabel(y_label[0])

    # subplot has 3 rows and 1 columns, plot location 2
    axes2 = scatter_plot.add_subplot(3, 1, 2)
    axes2.scatter(axes2_data[0], axes2_data[1])
    axes2.set_title(subplot_title[1])
    axes2.set_xlabel(x_label[1])
    axes2.set_ylabel(y_label[1])

    # subplot has 3 rows and 1 columns, plot location 3
    axes3 = scatter_plot.add_subplot(3, 1, 3)
    axes3.scatter(axes3_data[0], axes3_data[1])
    axes3.set_title(subplot_title[2])
    axes3.set_xlabel(x_label[2])
    axes3.set_ylabel(y_label[2])

    # add a title for the entire figure
    scatter_plot.suptitle(sup_title)
    scatter_plot.savefig(file_path + filename + ".png")


# Create 2x2 subplot_scatter
def subplotScatterTwoByTwo(axes1_data, axes2_data, axes3_data, axes4_data, x_label, y_label, subplot_title, sup_title, file_path, filename):
    """This plots distribution of the variable"""
    # create the figure where our subplots will go
    scatter_plot = plt.figure()
    axes1 = scatter_plot.add_subplot(2, 2, 1)
    axes1.scatter(axes1_data[0], axes1_data[1])
    axes1.set_title(subplot_title[0])
    axes1.set_xlabel(x_label[0])
    axes1.set_ylabel(y_label[0])

    # subplot has 2 rows and 2 columns, plot location 2
    axes2 = scatter_plot.add_subplot(2, 2, 2)
    axes2.scatter(axes2_data[0], axes2_data[1])
    axes2.set_title(subplot_title[1])
    axes2.set_xlabel(x_label[1])
    axes2.set_ylabel(y_label[1])

    # subplot has 2 rows and 2 columns, plot location 3
    axes3 = scatter_plot.add_subplot(2, 2, 3)
    axes3.scatter(axes3_data[0], axes3_data[1])
    axes3.set_title(subplot_title[2])
    axes3.set_xlabel(x_label[2])
    axes3.set_ylabel(y_label[2])

    # subplot has 2 rows and 2 columns, plot location 4
    axes4 = scatter_plot.add_subplot(2, 2, 4)
    axes4.scatter(axes4_data[0], axes4_data[1])
    axes4.set_title(subplot_title[3])
    axes4.set_xlabel(x_label[3])
    axes4.set_ylabel(y_label[3])

    # add a title for the entire figure
    scatter_plot.suptitle(sup_title)
    scatter_plot.savefig(file_path + filename + ".png")


# Box plot: Box plots are used when a discrete variable is plotted against a continuous variable.
# ================================================================================================
def pltBoxplot(x, y, x_label, y_label, label_param_1, label_param_2, title, file_path, filename):
    """This plots graph of a discrete variable
    against a continuous variable
    """
    box_plot = plt.figure()
    axes1 = box_plot.add_subplot(1, 1, 1)
    axes1.boxplot([x, y], labels=[label_param_1, label_param_2])
    axes1.set_title(title)
    axes1.set_xlabel(x_label)
    axes1.set_ylabel(y_label)
    box_plot.savefig(file_path + filename + ".png")


# Create 1x2 subplot_boxplot
def subplotBoxplotOnebyTwo(axes1_data, axes2_data,  x_label, y_label, label_param, subplot_title, sup_title, file_path, filename):
    """This plots graph of a discrete variable
    against a continuous variable
    """
    box_plot = plt.figure()
    axes1 = box_plot.add_subplot(1, 2, 1)
    axes1.boxplot([axes1_data[0], axes1_data[1]], labels=[label_param[0][0], label_param[0][1]])
    axes1.set_title(subplot_title[0])
    axes1.set_xlabel(x_label[0])
    axes1.set_ylabel(y_label[0])

    # subplot has 1 rows and 2 columns, plot location 2
    axes2 = box_plot.add_subplot(1, 2, 2)
    axes2.boxplot([axes2_data[0], axes2_data[1]], labels=[label_param[1][0], label_param[1][1]])
    axes2.set_title(subplot_title[1])
    axes2.set_xlabel(x_label[1])
    axes2.set_ylabel(y_label[1])

    # add a title for the entire figure
    box_plot.suptitle(sup_title)
    box_plot.savefig(file_path + filename + ".png")


# Create 2x1 subplot_boxplot
def subplotBoxplotTwoByOne(axes1_data, axes2_data, x_label, y_label, label_param, subplot_title, sup_title, file_path, filename):
    """This plots graph of a discrete variable
    against a continuous variable
    """
    # create the figure where our subplots will go
    box_plot = plt.figure()
    axes1 = box_plot.add_subplot(2, 1, 1)
    axes1.boxplot([axes1_data[0], axes1_data[1]], labels=[label_param[0][0], label_param[0][1]])
    axes1.set_title(subplot_title[0])
    axes1.set_xlabel(x_label[0])
    axes1.set_ylabel(y_label[0])

    # subplot has 2 rows and 1 columns, plot location 2
    axes2 = box_plot.add_subplot(2, 1, 2)
    axes2.boxplot([axes2_data[0], axes2_data[1]], labels=[label_param[1][0], label_param[1][1]])
    axes2.set_title(subplot_title[1])
    axes2.set_xlabel(x_label[1])
    axes2.set_ylabel(y_label[1])

    # add a title for the entire figure
    box_plot.suptitle(sup_title)
    box_plot.savefig(file_path + filename + ".png")


# Create 3x1 subplot_boxplot
def subplotBoxplotThreeByOne(axes1_data, axes2_data, axes3_data, x_label, y_label, label_param, subplot_title, sup_title, file_path, filename):
    """This plots graph of a discrete variable
    against a continuous variable
    """
    # create the figure where our subplots will go
    box_plot = plt.figure()
    axes1 = box_plot.add_subplot(3, 1, 1)
    axes1.boxplot([axes1_data[0], axes1_data[1]], labels=[label_param[0][0], label_param[0][1]])
    axes1.set_title(subplot_title[0])
    axes1.set_xlabel(x_label[0])
    axes1.set_ylabel(y_label[0])

    # subplot has 3 rows and 1 columns, plot location 2
    axes2 = box_plot.add_subplot(3, 1, 2)
    axes2.boxplot([axes2_data[0], axes2_data[1]], labels=[label_param[1][0], label_param[1][1]])
    axes2.set_title(subplot_title[1])
    axes2.set_xlabel(x_label[1])
    axes2.set_ylabel(y_label[1])

    # subplot has 3 rows and 1 columns, plot location 3
    axes3 = box_plot.add_subplot(3, 1, 3)
    axes3.boxplot([axes3_data[0], axes3_data[1]], labels=[label_param[2][0], label_param[2][1]])
    axes3.set_title(subplot_title[2])
    axes3.set_xlabel(x_label[2])
    axes3.set_ylabel(y_label[2])

    # add a title for the entire figure
    box_plot.suptitle(sup_title)
    box_plot.savefig(file_path + filename + ".png")


# Create 2x2 subplot_boxplot
def subplotBoxplotTwoByTwo(axes1_data, axes2_data, axes3_data, axes4_data, x_label, y_label, label_param, subplot_title, sup_title, file_path, filename):
    """This plots graph of a discrete variable
    against a continuous variable
    """
    # create the figure where our subplots will go
    box_plot = plt.figure()
    axes1 = box_plot.add_subplot(2, 2, 1)
    axes1.boxplot([axes1_data[0], axes1_data[1]], labels=[label_param[0][0], label_param[0][1]])
    axes1.set_title(subplot_title[0])
    axes1.set_xlabel(x_label[0])
    axes1.set_ylabel(y_label[0])

    # subplot has 2 rows and 2 columns, plot location 2
    axes2 = box_plot.add_subplot(2, 2, 2)
    axes2.boxplot([axes2_data[0], axes2_data[1]], labels=[label_param[1][0], label_param[1][1]])
    axes2.set_title(subplot_title[1])
    axes2.set_xlabel(x_label[1])
    axes2.set_ylabel(y_label[1])

    # subplot has 2 rows and 2 columns, plot location 3
    axes3 = box_plot.add_subplot(2, 2, 3)
    axes3.boxplot([axes3_data[0], axes3_data[1]], labels=[label_param[2][0], label_param[2][1]])
    axes3.set_title(subplot_title[2])
    axes3.set_xlabel(x_label[2])
    axes3.set_ylabel(y_label[2])

    # subplot has 2 rows and 2 columns, plot location 4
    axes4 = box_plot.add_subplot(2, 2, 4)
    axes4.boxplot([axes4_data[0], axes4_data[1]], labels=[label_param[3][0], label_param[3][1]])
    axes4.set_title(subplot_title[3])
    axes4.set_xlabel(x_label[3])
    axes4.set_ylabel(y_label[3])

    # add a title for the entire figure
    box_plot.suptitle(sup_title)
    box_plot.savefig(file_path + filename + ".png")


# Multivariate:
# ==========================================================================================
def pltScatterMultivar(x, y, x_label, y_label, color_var, size, title, file_path, filename):
    scatter_plot = plt.figure()
    axes1 = scatter_plot.add_subplot(1, 1, 1)
    axes1.scatter(x, y, c=color_var, s=size, alpha=0.5)
    axes1.set_title(title)
    axes1.set_xlabel(x_label)
    axes1.set_ylabel(y_label)
    scatter_plot.savefig(file_path + filename + ".png")

