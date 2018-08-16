#!/bin/bash
#SBATCH --job-name=bryozoa_corenlp
#SBATCH --account=uio
#SBATCH --output=logs/slurm-%j.base
#SBATCH --time=11:00:00
#SBATCH --nodes=37
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=3800M
#SBATCH --partition=normal
##SBATCH --mail-type=ALL
##SBATCH --mail-user=b.t.kopperud@nhm.uio.no

set -o errexit


arrayrun 0-37 annotate.sh
