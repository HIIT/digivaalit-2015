## loading environment in taito.csc.fi
module load finnish-process

cd $1

rm -rf *nlp ## clean old stuff

for file in *; do
   echo "$(sed 's/[,.:;!]//g' $file)" | finnish-process > $file.finnish_nlp
done
