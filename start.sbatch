#!/bin/bash
#SBATCH --job-name=bryozoa
#SBATCH --account=uio
#SBATCH --output=logs/slurm-%j.base
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=3800M
#SBATCH --partition=normal
##SBATCH --mail-type=ALL
##SBATCH --mail-user=b.t.kopperud@nhm.uio.no

set -o errexit

#module load python3

#~/natural_language_processing/start.sh &
#nlp_path = "~/natural_language_processing/"
java -mx48g -cp "/usit/abel/u1/bjorntko/natural_language_processing/*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -serverProperties /usit/abel/u1/bjorntko/natural_language_processing/server.prop &


module load python3
python3 -i run.py

ps aux | grep "CoreNLPServer" | awk '{print $2}' | xargs kill

