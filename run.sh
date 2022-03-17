#!/bin/bash
#SBATCH --job-name=musicgen
#SBATCH -p veu
#SBATCH --mem=20G
#SBATCH --cpus-per-task=2
#SBATCH --gres=gpu:1
#SBATCH --time=2-00:00:00

source ~/miniconda3/bin/activate
conda activate tfg
python3 train.py
