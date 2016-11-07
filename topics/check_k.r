source('topics.r')

library("argparser")

p <- arg_parser("Find the best fit of a topic model thing")

p <- add_argument(p, "--plot", help="create a plot", flag=TRUE)
p <- add_argument(p, "--method", help="choose method in use", default = "logll")
p <- add_argument(p, "folder", help="folders to analyse")

args <- parse_args( p )

print( args$method )

##for( path in commandArgs(trailingOnly=TRUE) ) {

  df = data.frame( k = integer(), ll =integer() )

  path <- args$folder;

  for( f in list.files( path, pattern = '*.rdata') ){
  	load( paste(path, f, sep = '') )
  	k <- model@k
  	ll <- check_fitness_ll( model )
  	row = c(k, ll)
  	df[ nrow(df)+1,] <- row
  }

  print("Examinging")
  print( path )

  print("Best fit k" )
  print( df$k[ which.max( df$ll ) ] )

  print("Best fit log likelihood")
  print( df$ll[ which.max( df$ll ) ] )
  print("") ## Empty line

  if( args$plot ) {

    library('ggplot2')

    g <- ggplot( df , aes(k , ll ) ) +
    geom_line() +
    xlab('Aiheiden määrä') + ylab('Loglikelihood') +
    theme_minimal() +
    xlim(10,30) ## TODO: make args

    ggsave( file = 'plot.pdf' , g)

  }

##}
