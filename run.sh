#!/bin/bash
#SBATCH --job-name=gansformer
#SBATCH --mem=20G
#SBATCH -c1
#SBATCH --gres=gpu:1,gpumem:16G
#SBATCH -t 1-00:00
python3 train.py -c config/train.yml config/base.yml -m dataset/
