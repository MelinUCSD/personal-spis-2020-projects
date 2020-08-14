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
                            c("Choose a value" = "", "Sepal length" = "Sepal Length", "Sepal width" = "Sepal Width","Petal length" = "Petal Length", "Petal width" = "Petal WIdth"),
                ),
                selectInput("y_feature", "Y Axis:",
                            c("Choose a value" = "", "Sepal length" = "Sepal Length", "Sepal width" = "Sepal Width","Petal length" = "Petal Length", "Petal width" = "Petal WIdth"),
                ),
                actionButton("button", "Plot!", style="color:#fff; background-color: #e95420; border-color: #c34113;
>                                border-radius: 10px; 
>                                border-width: 2px"),  
            ),
            mainPanel(
                imageOutput("plot")
            )
      ),
      tabPanel("Dataset",
               mainPanel(
                 fluidRow(
                   column(12, dataTableOutput('table')
                   )
                 )
              ),
      )
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
        if (input$x_feature != "" && input$y_feature != "") {
          title <- c(input$x_feature, input$y_feature)
          title <- paste(title, collapse=" vs ")
          model$plot(input$x_feature, input$y_feature, model$target, title)
        }
        
        output$plot <- renderImage({
            image_name <- normalizePath(file.path("./",
                           paste(title, ".png", sep="")))
            list(src = image_name)
        }, deleteFile = TRUE)
    })
    
    output$table <- renderDataTable(iris)
  } # server

  # Create Shiny object
  shinyApp(ui = ui, server = server)