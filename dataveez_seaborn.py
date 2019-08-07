import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})


# plots with Univariate variable: histogram, density(kde), rug, and count/bar  plot using seaborn libraby
# ========================================================================================================
# Histogram with kde (kernel Density Estimation) set to False
def plotHist(data, x_label, y_label, title, file_path, filename):
    """This Plots the histogram with kde (kernel Density Estimation) set to False """
    hist = sns.distplot(data, kde=False)
    hist.set_title(title)
    hist.set_xlabel(x_label)
    hist.set_ylabel(y_label)
    fig = hist.get_figure()
    fig.savefig(file_path + filename + ".png")


# Density Plot with hist=False
def plotDensity(data, x_label, y_label, title, file_path, filename):
    """This Plots the kde (kernel Density Estimation) with hist=False """
    # Density plot using sns.distplot()
    kde_plot = sns.distplot(data, hist=False)
    # Density plot using sns.kdeplot with shade=True
    # kde_plot = sns.kdeplot(data, shade=True)
    kde_plot.set_title(title)
    kde_plot.set_xlabel(x_label)
    kde_plot.set_ylabel(y_label)
    fig = kde_plot.get_figure()
    fig.savefig(file_path + filename + ".png")


# Density Plot and Histogram
def snsHistDensity(data, x_label, title, file_path, filename):
    """This Plots hist with kde (kernel Density Estimation)"""
    hist_kde = sns.distplot(data)
    hist_kde.set_title(title)
    hist_kde.set_xlabel(x_label)
    # hist_kde.set_ylabel(y_label)
    fig = hist_kde.get_figure()
    fig.savefig(file_path + filename + ".png")


# Rug plot : used with other plots to enhance a visualization
def HistDenRug(data, x_label, title, file_path, filename):
    """This Plots hist with kde (kernel Density Estimation) and rug plot"""
    hist_kde_rug = sns.distplot(data, rug=True)
    hist_kde_rug.set_title(title)
    hist_kde_rug.set_xlabel(x_label)
    fig = hist_kde_rug.get_figure()
    fig.savefig(file_path + filename + ".png")


# Count plot or Bar plot: used to count discrete variable
def plotCount(var, dataset, x_label, y_label, title, file_path, filename):
    count_plot = sns.countplot(var, data=dataset)
    count_plot.set_title(title)
    count_plot.set_xlabel(x_label)
    count_plot.set_ylabel(y_label)
    fig = count_plot.get_figure()
    fig.savefig(file_path + filename + ".png")


# Bivariate: Scatter plot, Hexbin plot, 2D Density plot, Bar plot, Box plot, Violin plot, Pairwise relationships
# ===============================================================================================================
# Scatter plot: Function regplot() is used to plot scatter plot and also fit a regression line.
# Set fit_reg=False to show only the scatter plot.
def plotScatter(x, y, dataset, x_label, y_label, title, file_path, filename):
    """plot scatter plot and also fit a regression line"""
    scatter = sns.regplot(x, y, data=dataset)
    # Set fit_reg=False to show only the scatter plot.
    scatter = sns.regplot(x, y, data=dataset, fit_reg=False)
    scatter.set_title(title)
    scatter.set_xlabel(x_label)
    scatter.set_ylabel(y_label)
    fig = scatter.get_figure()
    fig.savefig(file_path + filename + ".png")


# Scatter plot using lmplot()
def scatterlmplot(x, y, dataset, x_label, y_label, title, file_path, filename):
    """Plot scatter plot and also fit a regression line"""
    scatter = sns.lmplot(x, y, data=dataset)
    scatter.set_axis_labels(x_label, y_label)
    ax = plt.gca()
    ax.set_title(title)
    scatter.savefig(file_path + filename + ".png")


# Scatter plot with a univariate plot on each axis using jointplot()
def scatterJointplot(x, y, dataset, x_label, y_label, title, file_path, filename):
    """Scatter plot with a univariate plot on each axis using jointplot"""
    scatter = sns.jointplot(x, y, data=dataset)
    scatter.set_axis_labels(x_label, y_label)
    # add a title, set font size, and move the text above the total axes
    scatter.fig.suptitle(title, fontsize=20, y=1.03)
    scatter.savefig(file_path + filename + ".png")


# Hexbin plot using jointplot()
def plotHexbin(x, y, dataset, x_label, y_label, title, file_path, filename):
    """Plot hexbin plot"""
    hex = sns.jointplot(x, y, data=dataset, kind="hex")
    hex.set_axis_labels(x_label, y_label)
    # add a title, set font size, and move the text above the total axes
    hex.fig.suptitle(title, fontsize=20, y=1.03)
    hex.savefig(file_path + filename + ".png")


# 2D Density plot using kdetplot()
def twoDimDensity(x, y, x_label, y_label, title, file_path, filename):
    """Plot 2D kernel density plot"""
    # If cbar=True, draw a bivariate KDE plot, add a colorbar
    # shade=True, shade in the area under the KDE curve
    kde = sns.kdeplot(x, y, cbar=True, shade=True)
    kde.set_title(title)
    kde.set_xlabel(x_label)
    kde.set_ylabel(y_label)
    fig = kde.get_figure()
    fig.savefig(file_path + filename + ".png")


# Density (kde) plot with a univariate plot on each axis using jointplot()
def denJointplot(x, y, dataset, x_label, y_label, title, file_path, filename):
    """Density plot with a univariate plot on each axis using jointplot"""
    kde_joint = sns.jointplot(x, y, data=dataset, kind='kde')
    kde_joint.set_axis_labels(x_label, y_label)
    # add a title, set font size, and move the text above the total axes
    kde_joint.fig.suptitle(title, fontsize=20, y=1.03)
    kde_joint.savefig(file_path + filename + ".png")


# Bar plot using barplot()
def plotBar(x, y, dataset, x_label, y_label, title, file_path, filename):
    bar= sns.barplot(x, y, data=dataset)
    bar.set_title(title)
    bar.set_xlabel(x_label)
    bar.set_ylabel(y_label)
    fig = bar.get_figure()
    fig.savefig(file_path + filename + ".png")


# Box plot using boxplot()
def plotBox(x, y, dataset, x_label, y_label, title, file_path, filename):
    box= sns.boxplot(x, y, data=dataset)
    box.set_title(title)
    box.set_xlabel(x_label)
    box.set_ylabel(y_label)
    fig = box.get_figure()
    fig.savefig(file_path + filename + ".png")


# violin plot using violinplot()
def plotViolin(x, y, dataset, x_label, y_label, title, file_path, filename):
    violin= sns.violinplot(x, y, data=dataset)
    violin.set_title(title)
    violin.set_xlabel(x_label)
    violin.set_ylabel(y_label)
    fig = violin.get_figure()
    fig.savefig(file_path + filename + ".png")


# Pairwise relationship between numeric data using pairplot()
def plotPair(data, title, file_path, filename):
    """Plots a scatter plot between each pair of variables,
    and a histogram for the univariate
    """
    pair_plot= sns.pairplot(data)
    pair_plot.fig.suptitle(title, fontsize=20, y=1.03)
    pair_plot.savefig(file_path + filename + ".png")


# Pairwise relationship between numeric data using pairgrid()
# pairgrid() is used to manually assign the plots for the top half and bottom half
def plotPairGrid(data, file_path, filename):
    pair_grid= sns.PairGrid(data)
    # can also use pit.scatter instead of sns.regplot
    pair_grid = pair_grid.map_upper(sns.regplot)
    pair_grid = pair_grid.map_lower(sns.kdeplot)
    pair_grid = pair_grid.map_diag(sns.distplot, rug=True)
    pair_grid = pair_grid.savefig(file_path + filename + ".png")


# Multivariate : There is no de facto template for plotting multivariate data
# Possible ways to include more information is to use color, size, and shape to add more information to a plot
# =============================================================================================================
# In a violinplot, set hue parameter to color the plot by sex
def violinMultivar(x, y, color_var, dataset, x_label, y_label, title, file_path, filename):
    violin= sns.violinplot(x, y, hue=color_var, data=dataset, split=True)
    violin.set_title(title)
    violin.set_xlabel(x_label)
    violin.set_ylabel(y_label)
    fig = violin.get_figure()
    fig.savefig(file_path + filename + ".png")


# Scatter plot using lmplot() with hue parameter to plot multivariate plot
def scatterlmplotMultivar(x, y, color_var, dataset, x_label, y_label, title, file_path, filename):
    """Plot scatter plot without  fitting a regression line"""
    scatter = sns.lmplot(x, y, hue=color_var, data=dataset, fit_reg=False)
    scatter.set_axis_labels(x_label, y_label)
    ax = plt.gca()
    ax.set_title(title)
    scatter.savefig(file_path + filename + ".png")


# Pairwise plots using pairplot() with hue parameter (set to categorical variable)
def pairplotMultivar(data, hue_var, title, file_path, filename):
    pair_plot= sns.pairplot(data, hue=hue_var)
    pair_plot.fig.suptitle(title, fontsize=18, y=1.03)
    pair_plot.savefig(file_path + filename + ".png")


# Scatter plot using lmplot() with size and shape parameter to plot multivariate plot
def lmplotMultivar(x, y, color_var, dataset, x_label, y_label, title, file_path, filename):
    """Plot scatter plot without  fitting a regression line"""
    scatter = sns.lmplot(x, y, data=dataset,
                         hue=color_var,  fit_reg=False,
                         markers='o',
                         scatter_kws={'s': dataset['size']*10})
    scatter.set_axis_labels(x_label, y_label)
    ax = plt.gca()
    ax.set_title(title, fontsize=20, y=1.03)
    scatter.savefig(file_path + filename + ".png")


# Multiple plots over a categorical variable using lmplot()
def lmplotFacet(x, y, z, dataset, file_path, filename):
    """Plot scatter plot without  fitting a regression line"""
    data_set = sns.lmplot(x, y, data=dataset, fit_reg=False,
                          col=z,
                          col_wrap=2)
    data_set.savefig(file_path + filename + ".png")


# Create FacetGrid with histogram
def facetGridHist(x, dataset, col_var, file_path, filename):
    facet = sns.FacetGrid(data=dataset, col=col_var)
    # for each value in time, plot a histogram of x
    facet.map(sns.distplot, x, rug=True)
    facet.savefig(file_path + filename + ".png")


# Create FacetGrid with scatter
def facetGridScatter(x, y, dataset, col_var, hue_var, file_path, filename):
    facet = sns.FacetGrid(data=dataset, col=col_var, hue=hue_var)
    facet = facet.map(plt.scatter, x, y)
    facet = facet.add_legend()
    facet.savefig(file_path + filename + ".png")


# Multiple plots over a categorical variable using lmplot()
def sns_lmplot_facet_scatter(x, y, z, hue_var, dataset, file_path, filename):
    """Plot scatter plot without  fitting a regression line"""
    data_set = sns.lmplot(x, y, data=dataset, fit_reg=False,
                          hue=hue_var, col=z)
    data_set.savefig(file_path + filename + ".png")


# Scatter plot with one variable faceted on the x axis, and another variable faceted on the y axis
def plotFacetGrid(x, y, dataset, col_var, row_var, hue_var, file_path, filename):
    facet = sns.FacetGrid(data=dataset, col=col_var, row=row_var, hue=hue_var)
    facet = facet.map(plt.scatter, x, y)
    facet = facet.add_legend()
    facet.savefig(file_path + filename + ".png")
