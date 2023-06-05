library(plotly)

# Load the dataset
data <- read.csv('materials_data.csv')

# Create a 3D scatter plot
plot_ly(data, x = ~property1, y = ~property2, z = ~property3, color = ~class,
        type = "scatter3d", mode = "markers") %>%
  layout(scene = list(xaxis = list(title = "Property 1"),
                      yaxis = list(title = "Property 2"),
                      zaxis = list(title = "Property 3")))

