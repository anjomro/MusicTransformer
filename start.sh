mkdir dataset
mkdir dataset/processed
mkdir model_dir

pip install -r requirements.txt

sh scrape.sh dataset
python preprocess.py dataset dataset/processed

python train.py -c config/base.yml config/config-train.yml -m model_dir
