source('topics.r')

df = data.frame( k = integer(), ll =integer() )

path <- commandArgs(trailingOnly=TRUE)[0]

for( f in list.files(path) ){
	load(f)
	k <- model@k
	ll <- check_fitness_model( model )
	row = c(k, ll)
	df[ nrow(df)+1,] <- row
}

print("Best fit log likelihood", which.max( df$ll ) )
print("Best fit k", df$k[ which.max( df$ll ) ] )
