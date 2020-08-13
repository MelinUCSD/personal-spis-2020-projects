# Load R packages
library(reticulate)
library(shiny)
library(shinythemes)

# Reticulate Python libraries imports
path_to_python <- "/Users/matias/miniconda3/bin/python"
use_python(path_to_python)

  # Define UI
  ui <- fluidPage(theme = shinytheme("united"),
    navbarPage(
      # theme = "cerulean",  # <--- To use a theme, uncomment this
      "Iris Flower Classifier",
      tabPanel("Model",
               sidebarPanel(
                 tags$h3("Input:"),
                 textInput("txt1", "Sepal Length:", ""),
                 textInput("txt2", "Sepal Width:", ""),
                 textInput("txt3", "Petal Length:", ""),
                 textInput("txt4", "Petal Width:", ""),
                 
               ), # sidebarPanel
               mainPanel(
                            h1("Prediction"),
                            h4("Iris Flower Class:"),
                            verbatimTextOutput("txtout1"),
                            h4("Model Accuracy:"),
                            verbatimTextOutput("txtout2"),

               ) # mainPanel
               
      ), # Navbar 1, tabPanel
      tabPanel("Plot",
            sidebarPanel(
                selectInput("x_feature", "X-Axis:",
                    c("Choose a value" = "", "Sepal length" = "sl", "Sepal width" = "sw", "Petal length" = "pl", "Petal width" = "pw"),
                ),
                selectInput("y_feature", "Y Axis:",
                    c("Choose a value" = "", "Sepal length" = "sl", "Sepal width" = "sw", "Petal length" = "pl", "Petal width" = "pw"),
                ),
                actionButton("button", "Plot!", style="color:#fff; background-color: #e95420; border-color: #c34113;
>                                border-radius: 10px; 
>                                border-width: 2px"),  
            ),
            mainPanel(
                textOutput("result"),
                imageOutput("plot")
            )
      ),
      tabPanel("Dataset", "TODO: information about dataset")
      ) # navbarPage
  ) # fluidPage
  
  # Define server function  
  server <- function(input, output) {
    model <- import("main")
    output$txtout1 <- renderText({
      sepal_length <- input$txt1
      sepal_width <- input$txt2
      petal_length <- input$txt3
      petal_width <- input$txt4
      if (sepal_length != '' & sepal_width != '' & petal_length != '' & petal_width != '' ) {
        paste( model$predict(model$knn, as.numeric(sepal_length), as.numeric(sepal_width), as.numeric(petal_length), as.numeric(petal_width)) )
      } else {
          print( "Please enter all the values...")
      }
    })

    output$txtout2 <- renderText({
        paste( model$score(model$knn, model$x_test, model$y_test) )
    })

    observeEvent(input$button, {
        output$result <- renderText({
            if (input$x_feature != "" && input$y_feature != "") {
                paste( "X-Axis:", input$x_feature, "Y-Axis:", input$y_feature )
                if (input$x_feature == "sl") {
                    x_index <- 0
                } else if (input$x_feature == "sw") {
                    x_index <- 1
                } else if (input$x_feature == "pl") {
                    x_index <- 2
                } else if (input$x_feature == "pw") {
                    x_index <- 3
                }

                if (input$y_feature == "sl") {
                    y_index <- 0
                } else if (input$y_feature == "sw") {
                    y_index <- 1
                } else if (input$y_feature == "pl") {
                    y_index <- 2
                } else if (input$y_feature == "pw") {
                    y_index <- 3
                }

                title <- c(input$x_feature, input$y_feature)
                model$plot(model$features_list[x_index], model$features_list[y_index], model$target, 
                            title, model$labels_list[x_index], model$labels_list[y_index])

                output$plot <- renderImage({
                    map_harvest(lm_map_prod_filter())
                    list(src = title)
                })
            }
        })
    })
  } # server

  # Create Shiny object
  shinyApp(ui = ui, server = server)