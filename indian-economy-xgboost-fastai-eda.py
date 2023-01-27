14.7s 1 Collecting lazypredict
15.0s 2 Downloading lazypredict-0.2.12-py2.py3-none-any.whl (12 kB)
15.0s 3 Requirement already satisfied: lightgbm in /opt/conda/lib/python3.7/site-packages (from lazypredict) (3.3.2)
15.0s 4 Requirement already satisfied: click in /opt/conda/lib/python3.7/site-packages (from lazypredict) (8.0.4)
15.0s 5 Requirement already satisfied: pandas in /opt/conda/lib/python3.7/site-packages (from lazypredict) (1.3.5)
15.0s 6 Requirement already satisfied: tqdm in /opt/conda/lib/python3.7/site-packages (from lazypredict) (4.64.0)
15.0s 7 Requirement already satisfied: joblib in /opt/conda/lib/python3.7/site-packages (from lazypredict) (1.0.1)
15.0s 8 Requirement already satisfied: xgboost in /opt/conda/lib/python3.7/site-packages (from lazypredict) (1.6.2)
15.0s 9 Requirement already satisfied: scikit-learn in /opt/conda/lib/python3.7/site-packages (from lazypredict) (1.0.2)
15.0s 10 Requirement already satisfied: importlib-metadata in /opt/conda/lib/python3.7/site-packages (from click->lazypredict) (4.12.0)
15.0s 11 Requirement already satisfied: numpy in /opt/conda/lib/python3.7/site-packages (from lightgbm->lazypredict) (1.21.6)
15.0s 12 Requirement already satisfied: wheel in /opt/conda/lib/python3.7/site-packages (from lightgbm->lazypredict) (0.37.1)
15.0s 13 Requirement already satisfied: scipy in /opt/conda/lib/python3.7/site-packages (from lightgbm->lazypredict) (1.7.3)
15.1s 14 Requirement already satisfied: threadpoolctl>=2.0.0 in /opt/conda/lib/python3.7/site-packages (from scikit-learn->lazypredict) (3.1.0)
15.1s 15 Requirement already satisfied: python-dateutil>=2.7.3 in /opt/conda/lib/python3.7/site-packages (from pandas->lazypredict) (2.8.2)
15.1s 16 Requirement already satisfied: pytz>=2017.3 in /opt/conda/lib/python3.7/site-packages (from pandas->lazypredict) (2022.1)
15.1s 17 Requirement already satisfied: six>=1.5 in /opt/conda/lib/python3.7/site-packages (from python-dateutil>=2.7.3->pandas->lazypredict) (1.15.0)
15.2s 18 Requirement already satisfied: zipp>=0.5 in /opt/conda/lib/python3.7/site-packages (from importlib-metadata->click->lazypredict) (3.8.0)
15.2s 19 Requirement already satisfied: typing-extensions>=3.6.4 in /opt/conda/lib/python3.7/site-packages (from importlib-metadata->click->lazypredict) (4.3.0)
24.4s 20 Installing collected packages: lazypredict
24.7s 21 Successfully installed lazypredict-0.2.12
24.7s 22 [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
27.4s 23 [0mRequirement already satisfied: pandas in /opt/conda/lib/python3.7/site-packages (1.3.5)
27.8s 24 Requirement already satisfied: python-dateutil>=2.7.3 in /opt/conda/lib/python3.7/site-packages (from pandas) (2.8.2)
27.8s 25 Requirement already satisfied: pytz>=2017.3 in /opt/conda/lib/python3.7/site-packages (from pandas) (2022.1)
27.8s 26 Requirement already satisfied: numpy>=1.17.3 in /opt/conda/lib/python3.7/site-packages (from pandas) (1.21.6)
27.8s 27 Requirement already satisfied: six>=1.5 in /opt/conda/lib/python3.7/site-packages (from python-dateutil>=2.7.3->pandas) (1.15.0)
36.4s 28 [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
39.1s 29 [0mCollecting fast-tabnet
39.4s 30 Downloading fast_tabnet-0.2.0-py3-none-any.whl (23 kB)
39.6s 31 Collecting pytorch-tabnet>=2.0.1
39.6s 32 Downloading pytorch_tabnet-4.0-py3-none-any.whl (41 kB)
39.7s 33 [?25l     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/41.8 kB[0m [31m?[0m eta [36m-:--:--[0m[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m41.8/41.8 kB[0m [31m1.3 MB/s[0m eta [36m0:00:00[0m
39.7s 34 [?25hRequirement already satisfied: torch<2.0,>=1.2 in /opt/conda/lib/python3.7/site-packages (from pytorch-tabnet>=2.0.1->fast-tabnet) (1.11.0+cpu)
39.7s 35 Requirement already satisfied: tqdm<5.0,>=4.36 in /opt/conda/lib/python3.7/site-packages (from pytorch-tabnet>=2.0.1->fast-tabnet) (4.64.0)
39.7s 36 Requirement already satisfied: scipy>1.4 in /opt/conda/lib/python3.7/site-packages (from pytorch-tabnet>=2.0.1->fast-tabnet) (1.7.3)
39.7s 37 Requirement already satisfied: numpy<2.0,>=1.17 in /opt/conda/lib/python3.7/site-packages (from pytorch-tabnet>=2.0.1->fast-tabnet) (1.21.6)
39.7s 38 Requirement already satisfied: scikit_learn>0.21 in /opt/conda/lib/python3.7/site-packages (from pytorch-tabnet>=2.0.1->fast-tabnet) (1.0.2)
39.7s 39 Requirement already satisfied: joblib>=0.11 in /opt/conda/lib/python3.7/site-packages (from scikit_learn>0.21->pytorch-tabnet>=2.0.1->fast-tabnet) (1.0.1)
39.7s 40 Requirement already satisfied: threadpoolctl>=2.0.0 in /opt/conda/lib/python3.7/site-packages (from scikit_learn>0.21->pytorch-tabnet>=2.0.1->fast-tabnet) (3.1.0)
39.7s 41 Requirement already satisfied: typing-extensions in /opt/conda/lib/python3.7/site-packages (from torch<2.0,>=1.2->pytorch-tabnet>=2.0.1->fast-tabnet) (4.3.0)
48.1s 42 Installing collected packages: pytorch-tabnet, fast-tabnet
48.4s 43 Successfully installed fast-tabnet-0.2.0 pytorch-tabnet-4.0
48.4s 44 [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
50.9s 45 [0mRequirement already satisfied: fastai in /opt/conda/lib/python3.7/site-packages (2.7.9)
50.9s 46 Requirement already satisfied: torchvision>=0.8.2 in /opt/conda/lib/python3.7/site-packages (from fastai) (0.12.0+cpu)
50.9s 47 Requirement already satisfied: scipy in /opt/conda/lib/python3.7/site-packages (from fastai) (1.7.3)
50.9s 48 Requirement already satisfied: fastdownload<2,>=0.0.5 in /opt/conda/lib/python3.7/site-packages (from fastai) (0.0.7)
50.9s 49 Requirement already satisfied: fastcore<1.6,>=1.4.5 in /opt/conda/lib/python3.7/site-packages (from fastai) (1.5.26)
50.9s 50 Requirement already satisfied: matplotlib in /opt/conda/lib/python3.7/site-packages (from fastai) (3.5.3)
50.9s 51 Requirement already satisfied: pandas in /opt/conda/lib/python3.7/site-packages (from fastai) (1.3.5)
50.9s 52 Requirement already satisfied: pillow>6.0.0 in /opt/conda/lib/python3.7/site-packages (from fastai) (9.1.1)
50.9s 53 Requirement already satisfied: spacy<4 in /opt/conda/lib/python3.7/site-packages (from fastai) (3.3.1)
50.9s 54 Requirement already satisfied: torch<1.14,>=1.7 in /opt/conda/lib/python3.7/site-packages (from fastai) (1.11.0+cpu)
50.9s 55 Requirement already satisfied: scikit-learn in /opt/conda/lib/python3.7/site-packages (from fastai) (1.0.2)
50.9s 56 Requirement already satisfied: requests in /opt/conda/lib/python3.7/site-packages (from fastai) (2.28.1)
50.9s 57 Requirement already satisfied: fastprogress>=0.2.4 in /opt/conda/lib/python3.7/site-packages (from fastai) (1.0.3)
50.9s 58 Requirement already satisfied: pip in /opt/conda/lib/python3.7/site-packages (from fastai) (22.1.2)
50.9s 59 Requirement already satisfied: packaging in /opt/conda/lib/python3.7/site-packages (from fastai) (21.3)
50.9s 60 Requirement already satisfied: pyyaml in /opt/conda/lib/python3.7/site-packages (from fastai) (6.0)
51.0s 61 Requirement already satisfied: numpy>=1.15.0 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (1.21.6)
51.0s 62 Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (1.0.8)
51.2s 63 Collecting typing-extensions<4.2.0,>=3.7.4
51.5s 64 Downloading typing_extensions-4.1.1-py3-none-any.whl (26 kB)
51.5s 65 Requirement already satisfied: thinc<8.1.0,>=8.0.14 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (8.0.17)
51.5s 66 Requirement already satisfied: jinja2 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (3.1.2)
51.5s 67 Requirement already satisfied: langcodes<4.0.0,>=3.2.0 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (3.3.0)
51.5s 68 Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (1.0.3)
51.5s 69 Requirement already satisfied: blis<0.8.0,>=0.4.0 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (0.7.8)
51.5s 70 Requirement already satisfied: setuptools in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (59.8.0)
51.5s 71 Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (2.0.8)
51.5s 72 Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (2.0.6)
51.5s 73 Requirement already satisfied: srsly<3.0.0,>=2.4.3 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (2.4.4)
51.5s 74 Requirement already satisfied: typer<0.5.0,>=0.3.0 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (0.4.2)
51.5s 75 Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.9 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (3.0.10)
51.5s 76 Requirement already satisfied: pydantic!=1.8,!=1.8.1,<1.9.0,>=1.7.4 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (1.8.2)
51.5s 77 Requirement already satisfied: wasabi<1.1.0,>=0.9.1 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (0.10.1)
51.5s 78 Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (3.0.7)
51.5s 79 Requirement already satisfied: pathy>=0.3.5 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (0.6.2)
51.5s 80 Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in /opt/conda/lib/python3.7/site-packages (from spacy<4->fastai) (4.64.0)
51.6s 81 Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /opt/conda/lib/python3.7/site-packages (from packaging->fastai) (3.0.9)
51.6s 82 Requirement already satisfied: idna<4,>=2.5 in /opt/conda/lib/python3.7/site-packages (from requests->fastai) (3.3)
51.6s 83 Requirement already satisfied: certifi>=2017.4.17 in /opt/conda/lib/python3.7/site-packages (from requests->fastai) (2022.6.15.2)
51.6s 84 Requirement already satisfied: charset-normalizer<3,>=2 in /opt/conda/lib/python3.7/site-packages (from requests->fastai) (2.1.0)
51.6s 85 Requirement already satisfied: urllib3<1.27,>=1.21.1 in /opt/conda/lib/python3.7/site-packages (from requests->fastai) (1.26.12)
51.6s 86 Requirement already satisfied: python-dateutil>=2.7 in /opt/conda/lib/python3.7/site-packages (from matplotlib->fastai) (2.8.2)
51.6s 87 Requirement already satisfied: cycler>=0.10 in /opt/conda/lib/python3.7/site-packages (from matplotlib->fastai) (0.11.0)
51.6s 88 Requirement already satisfied: kiwisolver>=1.0.1 in /opt/conda/lib/python3.7/site-packages (from matplotlib->fastai) (1.4.3)
51.6s 89 Requirement already satisfied: fonttools>=4.22.0 in /opt/conda/lib/python3.7/site-packages (from matplotlib->fastai) (4.33.3)
51.6s 90 Requirement already satisfied: pytz>=2017.3 in /opt/conda/lib/python3.7/site-packages (from pandas->fastai) (2022.1)
51.7s 91 Requirement already satisfied: joblib>=0.11 in /opt/conda/lib/python3.7/site-packages (from scikit-learn->fastai) (1.0.1)
51.7s 92 Requirement already satisfied: threadpoolctl>=2.0.0 in /opt/conda/lib/python3.7/site-packages (from scikit-learn->fastai) (3.1.0)
51.7s 93 Requirement already satisfied: zipp>=0.5 in /opt/conda/lib/python3.7/site-packages (from catalogue<2.1.0,>=2.0.6->spacy<4->fastai) (3.8.0)
51.8s 94 Requirement already satisfied: smart-open<6.0.0,>=5.2.1 in /opt/conda/lib/python3.7/site-packages (from pathy>=0.3.5->spacy<4->fastai) (5.2.1)
51.9s 95 Requirement already satisfied: six>=1.5 in /opt/conda/lib/python3.7/site-packages (from python-dateutil>=2.7->matplotlib->fastai) (1.15.0)
52.0s 96 Requirement already satisfied: click<9.0.0,>=7.1.1 in /opt/conda/lib/python3.7/site-packages (from typer<0.5.0,>=0.3.0->spacy<4->fastai) (8.0.4)
52.0s 97 Requirement already satisfied: MarkupSafe>=2.0 in /opt/conda/lib/python3.7/site-packages (from jinja2->spacy<4->fastai) (2.1.1)
52.1s 98 Requirement already satisfied: importlib-metadata in /opt/conda/lib/python3.7/site-packages (from click<9.0.0,>=7.1.1->typer<0.5.0,>=0.3.0->spacy<4->fastai) (4.12.0)
60.2s 99 Installing collected packages: typing-extensions
60.2s 100 Attempting uninstall: typing-extensions
60.2s 101 Found existing installation: typing_extensions 4.3.0
60.2s 102 Uninstalling typing_extensions-4.3.0:
75.1s 103 Successfully uninstalled typing_extensions-4.3.0
75.4s 104 [31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
75.4s 105 tensorflow-io 0.21.0 requires tensorflow-io-gcs-filesystem==0.21.0, which is not installed.
75.4s 106 tensorflow 2.6.4 requires h5py~=3.1.0, but you have h5py 3.7.0 which is incompatible.
75.4s 107 tensorflow 2.6.4 requires numpy~=1.19.2, but you have numpy 1.21.6 which is incompatible.
75.4s 108 tensorflow 2.6.4 requires tensorboard<2.7,>=2.6.0, but you have tensorboard 2.10.0 which is incompatible.
75.4s 109 tensorflow 2.6.4 requires typing-extensions<3.11,>=3.7, but you have typing-extensions 4.1.1 which is incompatible.
75.4s 110 tensorflow-transform 1.9.0 requires pyarrow<6,>=1, but you have pyarrow 8.0.0 which is incompatible.
75.4s 111 tensorflow-transform 1.9.0 requires tensorflow!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,<2.10,>=1.15.5, but you have tensorflow 2.6.4 which is incompatible.
75.4s 112 tensorflow-serving-api 2.9.0 requires tensorflow<3,>=2.9.0, but you have tensorflow 2.6.4 which is incompatible.
75.4s 113 pandas-profiling 3.1.0 requires markupsafe~=2.0.1, but you have markupsafe 2.1.1 which is incompatible.
75.4s 114 flax 0.6.0 requires rich~=11.1, but you have rich 12.1.0 which is incompatible.
75.4s 115 flake8 4.0.1 requires importlib-metadata<4.3; python_version < "3.8", but you have importlib-metadata 4.12.0 which is incompatible.
75.4s 116 apache-beam 2.40.0 requires dill<0.3.2,>=0.3.1.1, but you have dill 0.3.5.1 which is incompatible.
75.4s 117 apache-beam 2.40.0 requires pyarrow<8.0.0,>=0.15.1, but you have pyarrow 8.0.0 which is incompatible.
75.4s 118 allennlp 2.10.0 requires protobuf==3.20.0, but you have protobuf 3.19.4 which is incompatible.
75.4s 119 aiobotocore 2.4.0 requires botocore<1.27.60,>=1.27.59, but you have botocore 1.27.72 which is incompatible.[0m[31m
75.4s 120 [0mSuccessfully installed typing-extensions-4.1.1
75.4s 121 [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
77.8s 122 [0mRequirement already satisfied: pandas-profiling in /opt/conda/lib/python3.7/site-packages (3.1.0)
77.8s 123 Requirement already satisfied: scipy>=1.4.1 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (1.7.3)
77.8s 124 Requirement already satisfied: tangled-up-in-unicode==0.1.0 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (0.1.0)
77.8s 125 Requirement already satisfied: matplotlib>=3.2.0 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (3.5.3)
77.8s 126 Requirement already satisfied: pydantic>=1.8.1 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (1.8.2)
77.9s 127 Requirement already satisfied: joblib~=1.0.1 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (1.0.1)
78.1s 128 Collecting markupsafe~=2.0.1
78.4s 129 Downloading MarkupSafe-2.0.1-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (31 kB)
78.4s 130 Requirement already satisfied: pandas!=1.0.0,!=1.0.1,!=1.0.2,!=1.1.0,>=0.25.3 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (1.3.5)
78.4s 131 Requirement already satisfied: visions[type_image_path]==0.7.4 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (0.7.4)
78.4s 132 Requirement already satisfied: multimethod>=1.4 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (1.4)
78.4s 133 Requirement already satisfied: htmlmin>=0.1.12 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (0.1.12)
78.4s 134 Requirement already satisfied: PyYAML>=5.0.0 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (6.0)
78.4s 135 Requirement already satisfied: tqdm>=4.48.2 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (4.64.0)
78.4s 136 Requirement already satisfied: numpy>=1.16.0 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (1.21.6)
78.4s 137 Requirement already satisfied: phik>=0.11.1 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (0.12.2)
78.4s 138 Requirement already satisfied: seaborn>=0.10.1 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (0.11.2)
78.4s 139 Requirement already satisfied: requests>=2.24.0 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (2.28.1)
78.4s 140 Requirement already satisfied: missingno>=0.4.2 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (0.4.2)
78.4s 141 Requirement already satisfied: jinja2>=2.11.1 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling) (3.1.2)
78.5s 142 Requirement already satisfied: networkx>=2.4 in /opt/conda/lib/python3.7/site-packages (from visions[type_image_path]==0.7.4->pandas-profiling) (2.5)
78.5s 143 Requirement already satisfied: attrs>=19.3.0 in /opt/conda/lib/python3.7/site-packages (from visions[type_image_path]==0.7.4->pandas-profiling) (21.4.0)
78.5s 144 Requirement already satisfied: imagehash in /opt/conda/lib/python3.7/site-packages (from visions[type_image_path]==0.7.4->pandas-profiling) (4.2.1)
78.5s 145 Requirement already satisfied: Pillow in /opt/conda/lib/python3.7/site-packages (from visions[type_image_path]==0.7.4->pandas-profiling) (9.1.1)
78.5s 146 Requirement already satisfied: cycler>=0.10 in /opt/conda/lib/python3.7/site-packages (from matplotlib>=3.2.0->pandas-profiling) (0.11.0)
78.5s 147 Requirement already satisfied: python-dateutil>=2.7 in /opt/conda/lib/python3.7/site-packages (from matplotlib>=3.2.0->pandas-profiling) (2.8.2)
78.5s 148 Requirement already satisfied: fonttools>=4.22.0 in /opt/conda/lib/python3.7/site-packages (from matplotlib>=3.2.0->pandas-profiling) (4.33.3)
78.5s 149 Requirement already satisfied: pyparsing>=2.2.1 in /opt/conda/lib/python3.7/site-packages (from matplotlib>=3.2.0->pandas-profiling) (3.0.9)
78.5s 150 Requirement already satisfied: packaging>=20.0 in /opt/conda/lib/python3.7/site-packages (from matplotlib>=3.2.0->pandas-profiling) (21.3)
78.5s 151 Requirement already satisfied: kiwisolver>=1.0.1 in /opt/conda/lib/python3.7/site-packages (from matplotlib>=3.2.0->pandas-profiling) (1.4.3)
78.6s 152 Requirement already satisfied: pytz>=2017.3 in /opt/conda/lib/python3.7/site-packages (from pandas!=1.0.0,!=1.0.1,!=1.0.2,!=1.1.0,>=0.25.3->pandas-profiling) (2022.1)
78.6s 153 Requirement already satisfied: typing-extensions>=3.7.4.3 in /opt/conda/lib/python3.7/site-packages (from pydantic>=1.8.1->pandas-profiling) (4.1.1)
78.6s 154 Requirement already satisfied: charset-normalizer<3,>=2 in /opt/conda/lib/python3.7/site-packages (from requests>=2.24.0->pandas-profiling) (2.1.0)
78.6s 155 Requirement already satisfied: certifi>=2017.4.17 in /opt/conda/lib/python3.7/site-packages (from requests>=2.24.0->pandas-profiling) (2022.6.15.2)
78.6s 156 Requirement already satisfied: idna<4,>=2.5 in /opt/conda/lib/python3.7/site-packages (from requests>=2.24.0->pandas-profiling) (3.3)
78.6s 157 Requirement already satisfied: urllib3<1.27,>=1.21.1 in /opt/conda/lib/python3.7/site-packages (from requests>=2.24.0->pandas-profiling) (1.26.12)
78.8s 158 Requirement already satisfied: decorator>=4.3.0 in /opt/conda/lib/python3.7/site-packages (from networkx>=2.4->visions[type_image_path]==0.7.4->pandas-profiling) (5.1.1)
78.9s 159 Requirement already satisfied: six>=1.5 in /opt/conda/lib/python3.7/site-packages (from python-dateutil>=2.7->matplotlib>=3.2.0->pandas-profiling) (1.15.0)
78.9s 160 Requirement already satisfied: PyWavelets in /opt/conda/lib/python3.7/site-packages (from imagehash->visions[type_image_path]==0.7.4->pandas-profiling) (1.3.0)
87.1s 161 Installing collected packages: markupsafe
87.1s 162 Attempting uninstall: markupsafe
87.1s 163 Found existing installation: MarkupSafe 2.1.1
87.1s 164 Uninstalling MarkupSafe-2.1.1:
87.1s 165 Successfully uninstalled MarkupSafe-2.1.1
87.4s 166 [31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
87.4s 167 beatrix-jupyterlab 3.1.7 requires google-cloud-bigquery-storage, which is not installed.
87.4s 168 werkzeug 2.2.2 requires MarkupSafe>=2.1.1, but you have markupsafe 2.0.1 which is incompatible.[0m[31m
87.4s 169 [0mSuccessfully installed markupsafe-2.0.1
87.4s 170 [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
95.5s 171 [0mparam_dir: /kaggle/working/indian-economy-from-1960-to-2020
95.5s 172 CSV!
135.2s 173 Target Variable: Life expectancy at birth, total (years)
135.2s 174 CATS=====================
135.2s 175 []
135.2s 176 CONTS=====================
135.2s 177 ['GDP (current US$) ', ' GDP per capita (current US$) ', 'GDP growth (annual %)', 'Imports of goods and services (% of GDP)', 'Exports of goods and services (% of GDP)', ' Total reserves (includes gold, current US$) ', 'Inflation, consumer prices (annual %)', 'Population, total', 'Population growth (annual %)']
135.2s 178 9
135.2s 179 Looping through continuous variables to find breakpoint
135.2s 180 Continuous variables that made the cut : ['GDP (current US$) ', ' GDP per capita (current US$) ', 'GDP growth (annual %)', 'Imports of goods and services (% of GDP)', 'Exports of goods and services (% of GDP)', ' Total reserves (includes gold, current US$) ', 'Inflation, consumer prices (annual %)', 'Population, total', 'Population growth (annual %)']
135.2s 181 Categorical variables that made the cut : []
135.2s 182 Tabular Object size: 61
135.2s 183 problem with getting one batch of indian-economy-from-1960-to-2020
135.5s 184 {'Model': 'AdaBoostRegressor', 'R-Squared': 0.9953042384152673, 'Adjusted R-Squared': 0.97417331128397, 'RMSE': 0.6567302774174221, 'Time taken': 0.08003067970275879}
135.5s 185 {'Model': 'BaggingRegressor', 'R-Squared': 0.9941185242487313, 'Adjusted R-Squared': 0.9676518833680219, 'RMSE': 0.7349827989220789, 'Time taken': 0.02677440643310547}
135.5s 186 {'Model': 'BayesianRidge', 'R-Squared': 0.9928995163541363, 'Adjusted R-Squared': 0.9609473399477497, 'RMSE': 0.80756592471595, 'Time taken': 0.030564308166503906}
135.5s 187 {'Model': 'DecisionTreeRegressor', 'R-Squared': 0.9870878621050087, 'Adjusted R-Squared': 0.9289832415775476, 'RMSE': 1.0890130838148537, 'Time taken': 0.010102033615112305}
135.5s 188 {'Model': 'DummyRegressor', 'R-Squared': -0.03380491282321629, 'Adjusted R-Squared': -4.685927020527689, 'RMSE': 9.74436, 'Time taken': 0.009185314178466797}
135.5s 189 {'Model': 'ElasticNet', 'R-Squared': 0.8896854990604209, 'Adjusted R-Squared': 0.3932702448323151, 'RMSE': 3.1831002, 'Time taken': 0.013438940048217773}
135.5s 190 {'Model': 'ElasticNetCV', 'R-Squared': 0.9918418076537997, 'Adjusted R-Squared': 0.9551299420958983, 'RMSE': 0.8656274, 'Time taken': 0.06800341606140137}
135.5s 191 {'Model': 'ExtraTreeRegressor', 'R-Squared': 0.9901907357930674, 'Adjusted R-Squared': 0.9460490468618705, 'RMSE': 0.9491879931453738, 'Time taken': 0.010263442993164062}
135.7s 192 {'Model': 'ExtraTreesRegressor', 'R-Squared': 0.998391174651184, 'Adjusted R-Squared': 0.9911514605815119, 'RMSE': 0.38440450619500727, 'Time taken': 0.10863995552062988}
135.7s 193 {'Model': 'GammaRegressor', 'R-Squared': 0.8718626003145314, 'Adjusted R-Squared': 0.2952443017299229, 'RMSE': 3.430614928266922, 'Time taken': 0.013137578964233398}
135.7s 194 {'Model': 'GaussianProcessRegressor', 'R-Squared': -4.321253426748433, 'Adjusted R-Squared': -28.26689384711638, 'RMSE': 22.107569107188493, 'Time taken': 0.016227245330810547}
135.7s 195 {'Model': 'GradientBoostingRegressor', 'R-Squared': 0.9974419686347495, 'Adjusted R-Squared': 0.9859308274911225, 'RMSE': 0.4847155500810377, 'Time taken': 0.08495974540710449}
135.7s 196 {'Model': 'HistGradientBoostingRegressor', 'R-Squared': 0.8611249165147585, 'Adjusted R-Squared': 0.23618704083117192, 'RMSE': 3.5714632559174415, 'Time taken': 0.0772101879119873}
136.0s 197 {'Model': 'HuberRegressor', 'R-Squared': 0.9871957442351895, 'Adjusted R-Squared': 0.9295765932935424, 'RMSE': 1.0844541377108325, 'Time taken': 0.03726363182067871}
136.0s 198 {'Model': 'KNeighborsRegressor', 'R-Squared': 0.9351830308708156, 'Adjusted R-Squared': 0.6435066697894856, 'RMSE': 2.439936, 'Time taken': 0.01036381721496582}
136.0s 199 {'Model': 'KernelRidge', 'R-Squared': -34.16741319633389, 'Adjusted R-Squared': -192.42077257983638, 'RMSE': 56.833477, 'Time taken': 0.019480228424072266}
136.0s 200 {'Model': 'Lars', 'R-Squared': 0.5758341636271656, 'Adjusted R-Squared': -1.3329121000505895, 'RMSE': 6.2416854, 'Time taken': 0.013151884078979492}
136.0s 201 {'Model': 'LarsCV', 'R-Squared': 0.9915849854883395, 'Adjusted R-Squared': 0.9537174201858674, 'RMSE': 0.8791469, 'Time taken': 0.0232694149017334}
136.0s 202 {'Model': 'Lasso', 'R-Squared': 0.9637751924105279, 'Adjusted R-Squared': 0.8007635582579034, 'RMSE': 1.8240515, 'Time taken': 0.011208057403564453}
136.0s 203 {'Model': 'LassoCV', 'R-Squared': 0.993410614608737, 'Adjusted R-Squared': 0.9637583803480536, 'RMSE': 0.7779586, 'Time taken': 0.0577549934387207}
136.0s 204 {'Model': 'LassoLars', 'R-Squared': 0.19399391484341644, 'Adjusted R-Squared': -3.4330334683612094, 'RMSE': 8.604055, 'Time taken': 0.0098724365234375}
136.0s 205 {'Model': 'LassoLarsCV', 'R-Squared': 0.9897784809511165, 'Adjusted R-Squared': 0.9437816452311409, 'RMSE': 0.9689285, 'Time taken': 0.03041553497314453}
136.0s 206 {'Model': 'LassoLarsIC', 'R-Squared': 0.9892111691581981, 'Adjusted R-Squared': 0.9406614303700893, 'RMSE': 0.995454, 'Time taken': 0.020602941513061523}
136.2s 207 {'Model': 'LinearRegression', 'R-Squared': 0.9862025466695334, 'Adjusted R-Squared': 0.9241140066824339, 'RMSE': 1.125728, 'Time taken': 0.012321233749389648}
136.2s 208 {'Model': 'LinearSVR', 'R-Squared': 0.013366626213406008, 'Adjusted R-Squared': -4.426483555826267, 'RMSE': 9.519451394496704, 'Time taken': 0.010139226913452148}
136.2s 209 {'Model': 'MLPRegressor', 'R-Squared': -9.874714728428321, 'Adjusted R-Squared': -58.810931006355766, 'RMSE': 31.604065, 'Time taken': 0.12160515785217285}
136.2s 210 {'Model': 'NuSVR', 'R-Squared': 0.5694142822776708, 'Adjusted R-Squared': -1.368221447472811, 'RMSE': 6.288742755827331, 'Time taken': 0.010953903198242188}
136.2s 211 {'Model': 'OrthogonalMatchingPursuit', 'R-Squared': 0.9737318101173976, 'Adjusted R-Squared': 0.855524955645687, 'RMSE': 1.5532776502529277, 'Time taken': 0.009929895401000977}
136.2s 212 {'Model': 'OrthogonalMatchingPursuitCV', 'R-Squared': 0.9928653228648989, 'Adjusted R-Squared': 0.9607592757569441, 'RMSE': 0.8095080693401342, 'Time taken': 0.015090227127075195}
136.2s 213 {'Model': 'PassiveAggressiveRegressor', 'R-Squared': 0.9774163918435079, 'Adjusted R-Squared': 0.8757901551392936, 'RMSE': 1.4402261257352265, 'Time taken': 0.01176595687866211}
136.2s 214 {'Model': 'PoissonRegressor', 'R-Squared': 0.9812849942924377, 'Adjusted R-Squared': 0.897067468608407, 'RMSE': 1.311079424422957, 'Time taken': 0.014670848846435547}
136.4s 215 {'Model': 'QuantileRegressor', 'R-Squared': -0.008851666688451942, 'Adjusted R-Squared': -4.548684166786486, 'RMSE': 9.62604034889254, 'Time taken': 0.07637166976928711}
136.4s 216 {'Model': 'RANSACRegressor', 'R-Squared': 0.986202593067012, 'Adjusted R-Squared': 0.9241142618685658, 'RMSE': 1.1257261, 'Time taken': 0.03273177146911621}
136.7s 217 {'Model': 'RandomForestRegressor', 'R-Squared': 0.9961797187001369, 'Adjusted R-Squared': 0.9789884528507529, 'RMSE': 0.5923544987700319, 'Time taken': 0.18500947952270508}
136.7s 218 {'Model': 'Ridge', 'R-Squared': 0.9856089253285836, 'Adjusted R-Squared': 0.9208490893072097, 'RMSE': 1.1496897, 'Time taken': 0.011133432388305664}
136.7s 219 {'Model': 'RidgeCV', 'R-Squared': 0.9935989979815257, 'Adjusted R-Squared': 0.9647944888983915, 'RMSE': 0.7667574456404126, 'Time taken': 0.010361909866333008}
136.7s 220 {'Model': 'SGDRegressor', 'R-Squared': 0.9840828213490125, 'Adjusted R-Squared': 0.9124555174195687, 'RMSE': 1.2091134861536037, 'Time taken': 0.013721942901611328}
136.7s 221 {'Model': 'SVR', 'R-Squared': 0.6513873700954274, 'Adjusted R-Squared': -0.9173694644751496, 'RMSE': 5.658555480949922, 'Time taken': 0.009836435317993164}
136.7s 222 {'Model': 'TransformedTargetRegressor', 'R-Squared': 0.9862025466695334, 'Adjusted R-Squared': 0.9241140066824339, 'RMSE': 1.125728, 'Time taken': 0.010384321212768555}
136.7s 223 {'Model': 'TweedieRegressor', 'R-Squared': 0.8789838234026932, 'Adjusted R-Squared': 0.33441102871481265, 'RMSE': 3.333924293424935, 'Time taken': 0.011480331420898438}
137.1s 224 {'Model': 'XGBRegressor', 'R-Squared': 0.9911606673174509, 'Adjusted R-Squared': 0.9513836702459799, 'RMSE': 0.90103936, 'Time taken': 0.3905644416809082}
137.1s 225 {'Model': 'LGBMRegressor', 'R-Squared': 0.8447537963566359, 'Adjusted R-Squared': 0.14614587996149764, 'RMSE': 3.776108932557612, 'Time taken': 0.08512163162231445}
137.1s 226 Project: indian-economy-from-1960-to-2020
137.1s 227 indian-economy-from-1960-to-2020
137.1s 228 Target: Life expectancy at birth, total (years)
137.1s 229 Life expectancy at birth, total (years)
137.1s 230 Target Standard Deviation: 8.032773971557617
137.1s 231 Adjusted R-Squared  R-Squared  RMSE  Time Taken
137.1s 232 Model
137.1s 233 ExtraTreesRegressor                          0.99       1.00  0.38        0.11
137.1s 234 GradientBoostingRegressor                    0.99       1.00  0.48        0.08
137.1s 235 RandomForestRegressor                        0.98       1.00  0.59        0.19
137.1s 236 AdaBoostRegressor                            0.97       1.00  0.66        0.08
137.1s 237 BaggingRegressor                             0.97       0.99  0.73        0.03
137.1s 238 RidgeCV                                      0.96       0.99  0.77        0.01
137.1s 239 LassoCV                                      0.96       0.99  0.78        0.06
137.1s 240 BayesianRidge                                0.96       0.99  0.81        0.03
137.1s 241 OrthogonalMatchingPursuitCV                  0.96       0.99  0.81        0.02
137.1s 242 ElasticNetCV                                 0.96       0.99  0.87        0.07
137.1s 243 LarsCV                                       0.95       0.99  0.88        0.02
137.1s 244 XGBRegressor                                 0.95       0.99  0.90        0.39
137.1s 245 ExtraTreeRegressor                           0.95       0.99  0.95        0.01
137.1s 246 LassoLarsCV                                  0.94       0.99  0.97        0.03
137.1s 247 LassoLarsIC                                  0.94       0.99  1.00        0.02
137.1s 248 HuberRegressor                               0.93       0.99  1.08        0.04
137.1s 249 DecisionTreeRegressor                        0.93       0.99  1.09        0.01
137.1s 250 RANSACRegressor                              0.92       0.99  1.13        0.03
137.1s 251 TransformedTargetRegressor                   0.92       0.99  1.13        0.01
137.1s 252 LinearRegression                             0.92       0.99  1.13        0.01
137.1s 253 Ridge                                        0.92       0.99  1.15        0.01
137.1s 254 SGDRegressor                                 0.91       0.98  1.21        0.01
137.1s 255 PoissonRegressor                             0.90       0.98  1.31        0.01
137.1s 256 PassiveAggressiveRegressor                   0.88       0.98  1.44        0.01
137.1s 257 OrthogonalMatchingPursuit                    0.86       0.97  1.55        0.01
137.1s 258 Lasso                                        0.80       0.96  1.82        0.01
137.1s 259 KNeighborsRegressor                          0.64       0.94  2.44        0.01
137.1s 260 ElasticNet                                   0.39       0.89  3.18        0.01
137.1s 261 TweedieRegressor                             0.33       0.88  3.33        0.01
137.1s 262 GammaRegressor                               0.30       0.87  3.43        0.01
137.1s 263 HistGradientBoostingRegressor                0.24       0.86  3.57        0.08
137.1s 264 LGBMRegressor                                0.15       0.84  3.78        0.09
137.1s 265 SVR                                         -0.92       0.65  5.66        0.01
137.1s 266 Lars                                        -1.33       0.58  6.24        0.01
137.1s 267 NuSVR                                       -1.37       0.57  6.29        0.01
137.1s 268 LassoLars                                   -3.43       0.19  8.60        0.01
137.1s 269 LinearSVR                                   -4.43       0.01  9.52        0.01
137.1s 270 QuantileRegressor                           -4.55      -0.01  9.63        0.08
137.1s 271 DummyRegressor                              -4.69      -0.03  9.74        0.01
137.1s 272 GaussianProcessRegressor                   -28.27      -4.32 22.11        0.02
137.1s 273 MLPRegressor                               -58.81      -9.87 31.60        0.12
137.1s 274 KernelRidge                               -192.42     -34.17 56.83        0.02
137.1s 275 LEARNING RATE: 0.1
137.1s 276 0%|          | 0/42 [00:00<?, ?it/s]  5%|▍         | 2/42 [00:00<00:02, 18.65it/s] 17%|█▋        | 7/42 [00:00<00:01, 30.80it/s] 24%|██▍       | 10/42 [00:00<00:01, 26.79it/s] 31%|███       | 13/42 [00:00<00:01, 21.95it/s] 43%|████▎     | 18/42 [00:00<00:00, 29.25it/s] 52%|█████▏    | 22/42 [00:00<00:00, 31.29it/s] 62%|██████▏   | 26/42 [00:00<00:00, 28.46it/s] 76%|███████▌  | 32/42 [00:01<00:00, 33.05it/s] 86%|████████▌ | 36/42 [00:01<00:00, 25.78it/s] 98%|█████████▊| 41/42 [00:01<00:00, 18.12it/s]100%|██████████| 42/42 [00:01<00:00, 22.80it/s]
137.2s 277 Better model found at epoch 0 with _rmse value: 103.70939636230469.
137.2s 278 No improvement since epoch 0: early stopping
137.7s 279 XGBoost Predictions vs Actual==========
137.7s 280 actual  predicted
137.7s 281 0   69.73      69.50
137.7s 282 1   57.18      58.96
137.7s 283 2   58.15      58.19
137.7s 284 3   65.12      65.61
137.7s 285 4   48.06      49.85
137.7s 286 XGBoost RMSE:  0.90577847
138.1s 287 Target Variable: Population growth (annual %)
138.1s 288 CATS=====================
138.1s 289 []
138.1s 290 CONTS=====================
138.1s 291 ['GDP (current US$) ', ' GDP per capita (current US$) ', 'GDP growth (annual %)', 'Imports of goods and services (% of GDP)', 'Exports of goods and services (% of GDP)', ' Total reserves (includes gold, current US$) ', 'Inflation, consumer prices (annual %)', 'Population, total', 'Life expectancy at birth, total (years)']
138.1s 292 9
138.1s 293 Looping through continuous variables to find breakpoint
138.1s 294 Continuous variables that made the cut : ['GDP (current US$) ', ' GDP per capita (current US$) ', 'GDP growth (annual %)', 'Imports of goods and services (% of GDP)', 'Exports of goods and services (% of GDP)', ' Total reserves (includes gold, current US$) ', 'Inflation, consumer prices (annual %)', 'Population, total', 'Life expectancy at birth, total (years)']
138.1s 295 Categorical variables that made the cut : []
138.1s 296 Tabular Object size: 61
138.1s 297 problem with getting one batch of indian-economy-from-1960-to-2020
138.4s 298 {'Model': 'AdaBoostRegressor', 'R-Squared': 0.9720249303299823, 'Adjusted R-Squared': 0.8461371168149026, 'RMSE': 0.07922092208456988, 'Time taken': 0.07578802108764648}
138.4s 299 {'Model': 'BaggingRegressor', 'R-Squared': 0.9765791746145354, 'Adjusted R-Squared': 0.8711854603799445, 'RMSE': 0.07248621164067909, 'Time taken': 0.027375221252441406}
138.4s 300 {'Model': 'BayesianRidge', 'R-Squared': 0.9666391120311514, 'Adjusted R-Squared': 0.8165151161713327, 'RMSE': 0.0865113532530762, 'Time taken': 0.012388467788696289}
138.4s 301 {'Model': 'DecisionTreeRegressor', 'R-Squared': 0.9800526834647598, 'Adjusted R-Squared': 0.890289759056179, 'RMSE': 0.06689544457326167, 'Time taken': 0.009516477584838867}
138.4s 302 {'Model': 'DummyRegressor', 'R-Squared': -0.03245087438927907, 'Adjusted R-Squared': -4.6784798091410345, 'RMSE': 0.48127022, 'Time taken': 0.008577823638916016}
138.4s 303 {'Model': 'ElasticNet', 'R-Squared': -0.03245087438927907, 'Adjusted R-Squared': -4.6784798091410345, 'RMSE': 0.48127022, 'Time taken': 0.009427070617675781}
138.4s 304 {'Model': 'ElasticNetCV', 'R-Squared': 0.9799869928677929, 'Adjusted R-Squared': 0.8899284607728609, 'RMSE': 0.0670055, 'Time taken': 0.07587122917175293}
138.4s 305 {'Model': 'ExtraTreeRegressor', 'R-Squared': 0.9659372508330409, 'Adjusted R-Squared': 0.8126548795817252, 'RMSE': 0.0874166486971843, 'Time taken': 0.010694026947021484}
138.6s 306 {'Model': 'ExtraTreesRegressor', 'R-Squared': 0.9761202078659253, 'Adjusted R-Squared': 0.8686611432625895, 'RMSE': 0.0731930046341675, 'Time taken': 0.11036348342895508}
138.6s 307 {'Model': 'GammaRegressor', 'R-Squared': 0.929320428889976, 'Adjusted R-Squared': 0.611262358894868, 'RMSE': 0.1259218969201374, 'Time taken': 0.012407779693603516}
138.6s 308 {'Model': 'GaussianProcessRegressor', 'R-Squared': -1.3721447438813437, 'Adjusted R-Squared': -12.04679609134739, 'RMSE': 0.7294993299204761, 'Time taken': 0.01220083236694336}
138.6s 309 {'Model': 'GradientBoostingRegressor', 'R-Squared': 0.9814975005225411, 'Adjusted R-Squared': 0.8982362528739762, 'RMSE': 0.06442723672906381, 'Time taken': 0.08793497085571289}
138.6s 310 {'Model': 'HistGradientBoostingRegressor', 'R-Squared': 0.5787699964126654, 'Adjusted R-Squared': -1.3167650197303407, 'RMSE': 0.30740714218474957, 'Time taken': 0.05599498748779297}
138.6s 311 {'Model': 'HuberRegressor', 'R-Squared': 0.9652453732585882, 'Adjusted R-Squared': 0.8088495529222349, 'RMSE': 0.08829998279341673, 'Time taken': 0.03429985046386719}
138.8s 312 {'Model': 'KNeighborsRegressor', 'R-Squared': 0.9429128317135953, 'Adjusted R-Squared': 0.6860205744247742, 'RMSE': 0.11316798, 'Time taken': 0.011638402938842773}
138.8s 313 {'Model': 'KernelRidge', 'R-Squared': -15.347386936668702, 'Adjusted R-Squared': -88.91062815167786, 'RMSE': 1.9150426, 'Time taken': 0.012798070907592773}
138.8s 314 {'Model': 'Lars', 'R-Squared': -215690.94646952164, 'Adjusted R-Squared': -1186304.7055823691, 'RMSE': 219.97395, 'Time taken': 0.01282358169555664}
138.8s 315 {'Model': 'LarsCV', 'R-Squared': 0.07058941245599293, 'Adjusted R-Squared': -4.111758231492039, 'RMSE': 0.45662335, 'Time taken': 0.02400970458984375}
138.8s 316 {'Model': 'Lasso', 'R-Squared': -0.03245087438927907, 'Adjusted R-Squared': -4.6784798091410345, 'RMSE': 0.48127022, 'Time taken': 0.010464906692504883}
138.8s 317 {'Model': 'LassoCV', 'R-Squared': 0.979093976910854, 'Adjusted R-Squared': 0.8850168730096969, 'RMSE': 0.06848414, 'Time taken': 0.07512044906616211}
138.8s 318 {'Model': 'LassoLars', 'R-Squared': -0.03245087438927907, 'Adjusted R-Squared': -4.6784798091410345, 'RMSE': 0.48127022, 'Time taken': 0.010651350021362305}
138.8s 319 {'Model': 'LassoLarsCV', 'R-Squared': 0.9621671657812347, 'Adjusted R-Squared': 0.791919411796791, 'RMSE': 0.09212738, 'Time taken': 0.033351898193359375}
138.8s 320 {'Model': 'LassoLarsIC', 'R-Squared': 0.9614577259735811, 'Adjusted R-Squared': 0.7880174928546964, 'RMSE': 0.09298716, 'Time taken': 0.01432180404663086}
139.1s 321 {'Model': 'LinearRegression', 'R-Squared': 0.9608669958461714, 'Adjusted R-Squared': 0.7847684771539427, 'RMSE': 0.09369705, 'Time taken': 0.01355290412902832}
139.1s 322 {'Model': 'LinearSVR', 'R-Squared': 0.9774878605654451, 'Adjusted R-Squared': 0.8761832331099482, 'RMSE': 0.07106613386756697, 'Time taken': 0.014151334762573242}
139.1s 323 {'Model': 'MLPRegressor', 'R-Squared': 0.8286253256831339, 'Adjusted R-Squared': 0.057439291257236125, 'RMSE': 0.19607744, 'Time taken': 0.11743974685668945}
139.1s 324 {'Model': 'NuSVR', 'R-Squared': 0.6470447038946858, 'Adjusted R-Squared': -0.941254128579228, 'RMSE': 0.2813935614065365, 'Time taken': 0.01211690902709961}
139.1s 325 {'Model': 'OrthogonalMatchingPursuit', 'R-Squared': 0.8789468529132538, 'Adjusted R-Squared': 0.33420769102289594, 'RMSE': 0.1647943610555787, 'Time taken': 0.010042667388916016}
139.1s 326 {'Model': 'OrthogonalMatchingPursuitCV', 'R-Squared': 0.9840849461325745, 'Adjusted R-Squared': 0.9124672037291596, 'RMSE': 0.059752813768569016, 'Time taken': 0.015369415283203125}
139.1s 327 {'Model': 'PassiveAggressiveRegressor', 'R-Squared': 0.9376983780446014, 'Adjusted R-Squared': 0.6573410792453078, 'RMSE': 0.11822354594167901, 'Time taken': 0.009610414505004883}
139.1s 328 {'Model': 'PoissonRegressor', 'R-Squared': 0.9402822752027215, 'Adjusted R-Squared': 0.671552513614968, 'RMSE': 0.11574598394292654, 'Time taken': 0.010988235473632812}
139.3s 329 {'Model': 'QuantileRegressor', 'R-Squared': -0.40340710758492415, 'Adjusted R-Squared': -6.718739091717083, 'RMSE': 0.5611075862754129, 'Time taken': 0.1064763069152832}
139.3s 330 {'Model': 'RANSACRegressor', 'R-Squared': 0.9608668598697759, 'Adjusted R-Squared': 0.7847677292837676, 'RMSE': 0.09369721, 'Time taken': 0.03161168098449707}
139.6s 331 {'Model': 'RandomForestRegressor', 'R-Squared': 0.9754779831290916, 'Adjusted R-Squared': 0.8651289072100039, 'RMSE': 0.07417070346898746, 'Time taken': 0.18497824668884277}
139.6s 332 {'Model': 'Ridge', 'R-Squared': 0.979467209222482, 'Adjusted R-Squared': 0.8870696507236508, 'RMSE': 0.06787007, 'Time taken': 0.01087641716003418}
139.6s 333 {'Model': 'RidgeCV', 'R-Squared': 0.9786294512758658, 'Adjusted R-Squared': 0.8824619820172617, 'RMSE': 0.06924081026507854, 'Time taken': 0.009810686111450195}
139.6s 334 {'Model': 'SGDRegressor', 'R-Squared': 0.9769036705961454, 'Adjusted R-Squared': 0.8729701882787995, 'RMSE': 0.07198231124429115, 'Time taken': 0.011053085327148438}
139.6s 335 {'Model': 'SVR', 'R-Squared': 0.6408733314563598, 'Adjusted R-Squared': -0.9751966769900209, 'RMSE': 0.2838429638566247, 'Time taken': 0.009281158447265625}
139.6s 336 {'Model': 'TransformedTargetRegressor', 'R-Squared': 0.9608669958461714, 'Adjusted R-Squared': 0.7847684771539427, 'RMSE': 0.09369705, 'Time taken': 0.00967717170715332}
139.6s 337 {'Model': 'TweedieRegressor', 'R-Squared': 0.9301579232458151, 'Adjusted R-Squared': 0.6158685778519832, 'RMSE': 0.12517363868207837, 'Time taken': 0.010217428207397461}
139.9s 338 {'Model': 'XGBRegressor', 'R-Squared': 0.9760424751918647, 'Adjusted R-Squared': 0.868233613555256, 'RMSE': 0.07331204, 'Time taken': 0.3635382652282715}
139.9s 339 {'Model': 'LGBMRegressor', 'R-Squared': 0.579960071586738, 'Adjusted R-Squared': -1.3102196062729408, 'RMSE': 0.3069725858077096, 'Time taken': 0.03958630561828613}
139.9s 340 Project: indian-economy-from-1960-to-2020
139.9s 341 indian-economy-from-1960-to-2020
139.9s 342 Target: Population growth (annual %)
139.9s 343 Population growth (annual %)
139.9s 344 Target Standard Deviation: 0.3982771933078766
139.9s 345 Adjusted R-Squared  R-Squared   RMSE  \
139.9s 346 Model
139.9s 347 OrthogonalMatchingPursuitCV                  0.91       0.98   0.06
139.9s 348 GradientBoostingRegressor                    0.90       0.98   0.06
139.9s 349 DecisionTreeRegressor                        0.89       0.98   0.07
139.9s 350 ElasticNetCV                                 0.89       0.98   0.07
139.9s 351 Ridge                                        0.89       0.98   0.07
139.9s 352 LassoCV                                      0.89       0.98   0.07
139.9s 353 RidgeCV                                      0.88       0.98   0.07
139.9s 354 LinearSVR                                    0.88       0.98   0.07
139.9s 355 SGDRegressor                                 0.87       0.98   0.07
139.9s 356 BaggingRegressor                             0.87       0.98   0.07
139.9s 357 ExtraTreesRegressor                          0.87       0.98   0.07
139.9s 358 XGBRegressor                                 0.87       0.98   0.07
139.9s 359 RandomForestRegressor                        0.87       0.98   0.07
139.9s 360 AdaBoostRegressor                            0.85       0.97   0.08
139.9s 361 BayesianRidge                                0.82       0.97   0.09
139.9s 362 ExtraTreeRegressor                           0.81       0.97   0.09
139.9s 363 HuberRegressor                               0.81       0.97   0.09
139.9s 364 LassoLarsCV                                  0.79       0.96   0.09
139.9s 365 LassoLarsIC                                  0.79       0.96   0.09
139.9s 366 TransformedTargetRegressor                   0.78       0.96   0.09
139.9s 367 LinearRegression                             0.78       0.96   0.09
139.9s 368 RANSACRegressor                              0.78       0.96   0.09
139.9s 369 KNeighborsRegressor                          0.69       0.94   0.11
139.9s 370 PoissonRegressor                             0.67       0.94   0.12
139.9s 371 PassiveAggressiveRegressor                   0.66       0.94   0.12
139.9s 372 TweedieRegressor                             0.62       0.93   0.13
139.9s 373 GammaRegressor                               0.61       0.93   0.13
139.9s 374 OrthogonalMatchingPursuit                    0.33       0.88   0.16
139.9s 375 MLPRegressor                                 0.06       0.83   0.20
139.9s 376 NuSVR                                       -0.94       0.65   0.28
139.9s 377 SVR                                         -0.98       0.64   0.28
139.9s 378 LGBMRegressor                               -1.31       0.58   0.31
139.9s 379 HistGradientBoostingRegressor               -1.32       0.58   0.31
139.9s 380 LarsCV                                      -4.11       0.07   0.46
139.9s 381 ElasticNet                                  -4.68      -0.03   0.48
139.9s 382 LassoLars                                   -4.68      -0.03   0.48
139.9s 383 DummyRegressor                              -4.68      -0.03   0.48
139.9s 384 Lasso                                       -4.68      -0.03   0.48
139.9s 385 QuantileRegressor                           -6.72      -0.40   0.56
139.9s 386 GaussianProcessRegressor                   -12.05      -1.37   0.73
139.9s 387 KernelRidge                                -88.91     -15.35   1.92
139.9s 388 Lars                                  -1186304.71 -215690.95 219.97
139.9s 389 
139.9s 390 Time Taken
139.9s 391 Model
139.9s 392 OrthogonalMatchingPursuitCV          0.02
139.9s 393 GradientBoostingRegressor            0.09
139.9s 394 DecisionTreeRegressor                0.01
139.9s 395 ElasticNetCV                         0.08
139.9s 396 Ridge                                0.01
139.9s 397 LassoCV                              0.08
139.9s 398 RidgeCV                              0.01
139.9s 399 LinearSVR                            0.01
139.9s 400 SGDRegressor                         0.01
139.9s 401 BaggingRegressor                     0.03
139.9s 402 ExtraTreesRegressor                  0.11
139.9s 403 XGBRegressor                         0.36
139.9s 404 RandomForestRegressor                0.18
139.9s 405 AdaBoostRegressor                    0.08
139.9s 406 BayesianRidge                        0.01
139.9s 407 ExtraTreeRegressor                   0.01
139.9s 408 HuberRegressor                       0.03
139.9s 409 LassoLarsCV                          0.03
139.9s 410 LassoLarsIC                          0.01
139.9s 411 TransformedTargetRegressor           0.01
139.9s 412 LinearRegression                     0.01
139.9s 413 RANSACRegressor                      0.03
139.9s 414 KNeighborsRegressor                  0.01
139.9s 415 PoissonRegressor                     0.01
139.9s 416 PassiveAggressiveRegressor           0.01
139.9s 417 TweedieRegressor                     0.01
139.9s 418 GammaRegressor                       0.01
139.9s 419 OrthogonalMatchingPursuit            0.01
139.9s 420 MLPRegressor                         0.12
139.9s 421 NuSVR                                0.01
139.9s 422 SVR                                  0.01
139.9s 423 LGBMRegressor                        0.04
139.9s 424 HistGradientBoostingRegressor        0.06
139.9s 425 LarsCV                               0.02
139.9s 426 ElasticNet                           0.01
139.9s 427 LassoLars                            0.01
139.9s 428 DummyRegressor                       0.01
139.9s 429 Lasso                                0.01
139.9s 430 QuantileRegressor                    0.11
139.9s 431 GaussianProcessRegressor             0.01
139.9s 432 KernelRidge                          0.01
139.9s 433 Lars                                 0.01
139.9s 434 LEARNING RATE: 0.1
139.9s 435 0%|          | 0/42 [00:00<?, ?it/s]  5%|▍         | 2/42 [00:00<00:02, 19.35it/s] 17%|█▋        | 7/42 [00:00<00:01, 33.77it/s] 26%|██▌       | 11/42 [00:00<00:01, 30.31it/s] 36%|███▌      | 15/42 [00:00<00:01, 25.43it/s] 48%|████▊     | 20/42 [00:00<00:00, 29.15it/s] 62%|██████▏   | 26/42 [00:00<00:00, 29.20it/s] 76%|███████▌  | 32/42 [00:01<00:00, 31.45it/s] 86%|████████▌ | 36/42 [00:01<00:00, 25.54it/s] 98%|█████████▊| 41/42 [00:01<00:00, 19.03it/s]100%|██████████| 42/42 [00:01<00:00, 23.91it/s]
139.9s 436 Better model found at epoch 0 with _rmse value: 38.60154342651367.
140.0s 437 No improvement since epoch 0: early stopping
140.5s 438 XGBoost Predictions vs Actual==========
140.5s 439 actual  predicted
140.5s 440 0    2.01       1.97
140.5s 441 1    2.24       2.24
140.5s 442 2    2.15       2.19
140.5s 443 3    2.34       2.32
140.5s 444 4    1.74       1.86
140.5s 445 XGBoost RMSE:  0.07331204
140.8s 446 Target Variable: Population, total
140.8s 447 CATS=====================
140.8s 448 []
140.8s 449 CONTS=====================
140.8s 450 ['GDP (current US$) ', ' GDP per capita (current US$) ', 'GDP growth (annual %)', 'Imports of goods and services (% of GDP)', 'Exports of goods and services (% of GDP)', ' Total reserves (includes gold, current US$) ', 'Inflation, consumer prices (annual %)', 'Population growth (annual %)', 'Life expectancy at birth, total (years)']
140.8s 451 9
140.8s 452 Looping through continuous variables to find breakpoint
140.8s 453 Continuous variables that made the cut : ['GDP (current US$) ', ' GDP per capita (current US$) ', 'GDP growth (annual %)', 'Imports of goods and services (% of GDP)', 'Exports of goods and services (% of GDP)', ' Total reserves (includes gold, current US$) ', 'Inflation, consumer prices (annual %)', 'Population growth (annual %)', 'Life expectancy at birth, total (years)']
140.8s 454 Categorical variables that made the cut : []
140.8s 455 Tabular Object size: 61
140.8s 456 problem with getting one batch of indian-economy-from-1960-to-2020
141.1s 457 {'Model': 'AdaBoostRegressor', 'R-Squared': 0.994781913096659, 'Adjusted R-Squared': 0.9713005220316244, 'RMSE': 22065425.903302643, 'Time taken': 0.07797694206237793}
141.1s 458 {'Model': 'BaggingRegressor', 'R-Squared': 0.996993393520616, 'Adjusted R-Squared': 0.9834636643633881, 'RMSE': 16749234.200037217, 'Time taken': 0.028387784957885742}
141.1s 459 {'Model': 'BayesianRidge', 'R-Squared': -0.03098000915738397, 'Adjusted R-Squared': -4.6703900503656115, 'RMSE': 310157139.67595994, 'Time taken': 0.011009454727172852}
141.1s 460 {'Model': 'DecisionTreeRegressor', 'R-Squared': 0.989759888982371, 'Adjusted R-Squared': 0.9436793894030404, 'RMSE': 30910710.89516892, 'Time taken': 0.009494781494140625}
141.1s 461 {'Model': 'DummyRegressor', 'R-Squared': -0.030980036507947117, 'Adjusted R-Squared': -4.670390200793709, 'RMSE': 310157150.0, 'Time taken': 0.008668899536132812}
141.1s 462 {'Model': 'ElasticNet', 'R-Squared': 0.9452660785646824, 'Adjusted R-Squared': 0.698963432105753, 'RMSE': 71463610.0, 'Time taken': 0.01112222671508789}
141.1s 463 {'Model': 'ElasticNetCV', 'R-Squared': -0.030941694105468986, 'Adjusted R-Squared': -4.67017931758008, 'RMSE': 310151360.0, 'Time taken': 0.05703234672546387}
141.1s 464 {'Model': 'ExtraTreeRegressor', 'R-Squared': 0.995191255099718, 'Adjusted R-Squared': 0.9735519030484487, 'RMSE': 21182271.49270786, 'Time taken': 0.010637283325195312}
141.4s 465 {'Model': 'ExtraTreesRegressor', 'R-Squared': 0.9995106571311895, 'Adjusted R-Squared': 0.9973086142215422, 'RMSE': 6757145.842134212, 'Time taken': 0.11365580558776855}
141.4s 466 {'Model': 'GammaRegressor', 'R-Squared': 0.8851517685959668, 'Adjusted R-Squared': 0.36833472727781724, 'RMSE': 103518701.69744334, 'Time taken': 0.012445211410522461}
141.4s 467 {'Model': 'GaussianProcessRegressor', 'R-Squared': 0.8658078243280991, 'Adjusted R-Squared': 0.2619430338045451, 'RMSE': 111897467.5694859, 'Time taken': 0.012127876281738281}
141.4s 468 {'Model': 'GradientBoostingRegressor', 'R-Squared': 0.9983478383570482, 'Adjusted R-Squared': 0.9909131109637652, 'RMSE': 12416035.004732624, 'Time taken': 0.08925795555114746}
141.4s 469 {'Model': 'HistGradientBoostingRegressor', 'R-Squared': 0.9042343000202554, 'Adjusted R-Squared': 0.47328865011140464, 'RMSE': 94528257.95052792, 'Time taken': 0.06958150863647461}
141.4s 470 {'Model': 'HuberRegressor', 'R-Squared': -0.033153275312549635, 'Adjusted R-Squared': -4.682343014219023, 'RMSE': 310483867.2373013, 'Time taken': 0.019364118576049805}
141.6s 471 {'Model': 'KNeighborsRegressor', 'R-Squared': 0.9750943072330553, 'Adjusted R-Squared': 0.8630186897818044, 'RMSE': 48206544.0, 'Time taken': 0.013355255126953125}
141.6s 472 {'Model': 'KernelRidge', 'R-Squared': -7.507942610016887, 'Adjusted R-Squared': -45.79368435509288, 'RMSE': 890982000.0, 'Time taken': 0.010386228561401367}
141.6s 473 {'Model': 'Lars', 'R-Squared': 0.9653404996600667, 'Adjusted R-Squared': 0.8093727481303671, 'RMSE': 56867980.0, 'Time taken': 0.010765552520751953}
141.6s 474 {'Model': 'LarsCV', 'R-Squared': 0.9945693332744402, 'Adjusted R-Squared': 0.970131333009421, 'RMSE': 22510402.0, 'Time taken': 0.0225827693939209}
141.6s 475 {'Model': 'Lasso', 'R-Squared': 0.9943240250472324, 'Adjusted R-Squared': 0.9687821377597781, 'RMSE': 23013192.0, 'Time taken': 0.01112222671508789}
141.6s 476 {'Model': 'LassoCV', 'R-Squared': 0.9945688377201674, 'Adjusted R-Squared': 0.9701286074609204, 'RMSE': 22511428.0, 'Time taken': 0.05896925926208496}
141.6s 477 {'Model': 'LassoLars', 'R-Squared': 0.9947682212443236, 'Adjusted R-Squared': 0.9712252168437799, 'RMSE': 22094354.0, 'Time taken': 0.013979196548461914}
141.6s 478 {'Model': 'LassoLarsCV', 'R-Squared': 0.9948672753341783, 'Adjusted R-Squared': 0.9717700143379806, 'RMSE': 21884198.0, 'Time taken': 0.026455163955688477}
141.6s 479 {'Model': 'LassoLarsIC', 'R-Squared': 0.99490602206582, 'Adjusted R-Squared': 0.97198312136201, 'RMSE': 21801440.0, 'Time taken': 0.014030933380126953}
141.6s 480 {'Model': 'LinearRegression', 'R-Squared': 0.994767848291846, 'Adjusted R-Squared': 0.9712231656051526, 'RMSE': 22095144.0, 'Time taken': 0.010638713836669922}
141.6s 481 {'Model': 'LinearSVR', 'R-Squared': -9.360995101998428, 'Adjusted R-Squared': -55.98547306099135, 'RMSE': 983235147.7673632, 'Time taken': 0.011050701141357422}
141.9s 482 {'Model': 'MLPRegressor', 'R-Squared': -9.360995987687375, 'Adjusted R-Squared': -55.98547793228056, 'RMSE': 983235200.0, 'Time taken': 0.12422537803649902}
141.9s 483 {'Model': 'NuSVR', 'R-Squared': -0.032053357423860396, 'Adjusted R-Squared': -4.6762934658312325, 'RMSE': 310318549.2200139, 'Time taken': 0.012069940567016602}
141.9s 484 {'Model': 'OrthogonalMatchingPursuit', 'R-Squared': 0.9727648794560297, 'Adjusted R-Squared': 0.8502068370081636, 'RMSE': 50410535.5862227, 'Time taken': 0.0100250244140625}
141.9s 485 {'Model': 'OrthogonalMatchingPursuitCV', 'R-Squared': 0.9947821887117191, 'Adjusted R-Squared': 0.971302037914455, 'RMSE': 22064843.156780142, 'Time taken': 0.01591181755065918}
141.9s 486 {'Model': 'PassiveAggressiveRegressor', 'R-Squared': -9.36001451861226, 'Adjusted R-Squared': -55.98007985236743, 'RMSE': 983188619.0867553, 'Time taken': 0.013838768005371094}
141.9s 487 {'Model': 'PoissonRegressor', 'R-Squared': 0.9977535982609531, 'Adjusted R-Squared': 0.9876447904352421, 'RMSE': 14477726.698789122, 'Time taken': 0.0237886905670166}
141.9s 488 {'Model': 'QuantileRegressor', 'R-Squared': -0.07312796475912564, 'Adjusted R-Squared': -4.902203806175191, 'RMSE': 316433472.2998559, 'Time taken': 0.09797787666320801}
141.9s 489 {'Model': 'RANSACRegressor', 'R-Squared': 0.9947678374322528, 'Adjusted R-Squared': 0.9712231058773906, 'RMSE': 22095164.0, 'Time taken': 0.024608135223388672}
142.3s 490 {'Model': 'RandomForestRegressor', 'R-Squared': 0.9979451405751975, 'Adjusted R-Squared': 0.988698273163586, 'RMSE': 13846745.78684295, 'Time taken': 0.1865983009338379}
142.3s 491 {'Model': 'Ridge', 'R-Squared': 0.9956165861170809, 'Adjusted R-Squared': 0.9758912236439451, 'RMSE': 20223806.0, 'Time taken': 0.010468244552612305}
142.3s 492 {'Model': 'RidgeCV', 'R-Squared': 0.994830310189175, 'Adjusted R-Squared': 0.9715667060404625, 'RMSE': 21962860.519320924, 'Time taken': 0.010290384292602539}
142.3s 493 {'Model': 'SGDRegressor', 'R-Squared': 0.994898309041342, 'Adjusted R-Squared': 0.9719406997273812, 'RMSE': 21817939.55695555, 'Time taken': 0.015411615371704102}
142.3s 494 {'Model': 'SVR', 'R-Squared': -0.07306850057743675, 'Adjusted R-Squared': -4.901876753175902, 'RMSE': 316424705.0704206, 'Time taken': 0.010306596755981445}
142.3s 495 {'Model': 'TransformedTargetRegressor', 'R-Squared': 0.994767848291846, 'Adjusted R-Squared': 0.9712231656051526, 'RMSE': 22095144.0, 'Time taken': 0.010366439819335938}
142.3s 496 {'Model': 'TweedieRegressor', 'R-Squared': 0.9088990518164621, 'Adjusted R-Squared': 0.49894478499054173, 'RMSE': 92197280.12333366, 'Time taken': 0.01320648193359375}
142.7s 497 {'Model': 'XGBRegressor', 'R-Squared': 0.9949116932932569, 'Adjusted R-Squared': 0.972014313112913, 'RMSE': 21789300.0, 'Time taken': 0.39494991302490234}
142.7s 498 {'Model': 'LGBMRegressor', 'R-Squared': 0.8698834042312809, 'Adjusted R-Squared': 0.2843587232720447, 'RMSE': 110185134.69034986, 'Time taken': 0.042664527893066406}
142.7s 499 Project: indian-economy-from-1960-to-2020
142.7s 500 indian-economy-from-1960-to-2020
142.7s 501 Target: Population, total
142.7s 502 Population, total
142.7s 503 Target Standard Deviation: 291408672.0
142.7s 504 Adjusted R-Squared  R-Squared         RMSE  \
142.7s 505 Model
142.7s 506 ExtraTreesRegressor                          1.00       1.00   6757145.84
142.7s 507 GradientBoostingRegressor                    0.99       1.00  12416035.00
142.7s 508 RandomForestRegressor                        0.99       1.00  13846745.79
142.7s 509 PoissonRegressor                             0.99       1.00  14477726.70
142.7s 510 BaggingRegressor                             0.98       1.00  16749234.20
142.7s 511 Ridge                                        0.98       1.00  20223806.00
142.7s 512 ExtraTreeRegressor                           0.97       1.00  21182271.49
142.7s 513 XGBRegressor                                 0.97       0.99  21789300.00
142.7s 514 LassoLarsIC                                  0.97       0.99  21801440.00
142.7s 515 SGDRegressor                                 0.97       0.99  21817939.56
142.7s 516 LassoLarsCV                                  0.97       0.99  21884198.00
142.7s 517 RidgeCV                                      0.97       0.99  21962860.52
142.7s 518 OrthogonalMatchingPursuitCV                  0.97       0.99  22064843.16
142.7s 519 AdaBoostRegressor                            0.97       0.99  22065425.90
142.7s 520 LassoLars                                    0.97       0.99  22094354.00
142.7s 521 LinearRegression                             0.97       0.99  22095144.00
142.7s 522 TransformedTargetRegressor                   0.97       0.99  22095144.00
142.7s 523 RANSACRegressor                              0.97       0.99  22095164.00
142.7s 524 LarsCV                                       0.97       0.99  22510402.00
142.7s 525 LassoCV                                      0.97       0.99  22511428.00
142.7s 526 Lasso                                        0.97       0.99  23013192.00
142.7s 527 DecisionTreeRegressor                        0.94       0.99  30910710.90
142.7s 528 KNeighborsRegressor                          0.86       0.98  48206544.00
142.7s 529 OrthogonalMatchingPursuit                    0.85       0.97  50410535.59
142.7s 530 Lars                                         0.81       0.97  56867980.00
142.7s 531 ElasticNet                                   0.70       0.95  71463608.00
142.7s 532 TweedieRegressor                             0.50       0.91  92197280.12
142.7s 533 HistGradientBoostingRegressor                0.47       0.90  94528257.95
142.7s 534 GammaRegressor                               0.37       0.89 103518701.70
142.7s 535 LGBMRegressor                                0.28       0.87 110185134.69
142.7s 536 GaussianProcessRegressor                     0.26       0.87 111897467.57
142.7s 537 ElasticNetCV                                -4.67      -0.03 310151360.00
142.7s 538 BayesianRidge                               -4.67      -0.03 310157139.68
142.7s 539 DummyRegressor                              -4.67      -0.03 310157152.00
142.7s 540 NuSVR                                       -4.68      -0.03 310318549.22
142.7s 541 HuberRegressor                              -4.68      -0.03 310483867.24
142.7s 542 SVR                                         -4.90      -0.07 316424705.07
142.7s 543 QuantileRegressor                           -4.90      -0.07 316433472.30
142.7s 544 KernelRidge                                -45.79      -7.51 890982016.00
142.7s 545 PassiveAggressiveRegressor                 -55.98      -9.36 983188619.09
142.7s 546 LinearSVR                                  -55.99      -9.36 983235147.77
142.7s 547 MLPRegressor                               -55.99      -9.36 983235200.00
142.7s 548 
142.7s 549 Time Taken
142.7s 550 Model
142.7s 551 ExtraTreesRegressor                  0.11
142.7s 552 GradientBoostingRegressor            0.09
142.7s 553 RandomForestRegressor                0.19
142.7s 554 PoissonRegressor                     0.02
142.7s 555 BaggingRegressor                     0.03
142.7s 556 Ridge                                0.01
142.7s 557 ExtraTreeRegressor                   0.01
142.7s 558 XGBRegressor                         0.39
142.7s 559 LassoLarsIC                          0.01
142.7s 560 SGDRegressor                         0.02
142.7s 561 LassoLarsCV                          0.03
142.7s 562 RidgeCV                              0.01
142.7s 563 OrthogonalMatchingPursuitCV          0.02
142.7s 564 AdaBoostRegressor                    0.08
142.7s 565 LassoLars                            0.01
142.7s 566 LinearRegression                     0.01
142.7s 567 TransformedTargetRegressor           0.01
142.7s 568 RANSACRegressor                      0.02
142.7s 569 LarsCV                               0.02
142.7s 570 LassoCV                              0.06
142.7s 571 Lasso                                0.01
142.7s 572 DecisionTreeRegressor                0.01
142.7s 573 KNeighborsRegressor                  0.01
142.7s 574 OrthogonalMatchingPursuit            0.01
142.7s 575 Lars                                 0.01
142.7s 576 ElasticNet                           0.01
142.7s 577 TweedieRegressor                     0.01
142.7s 578 HistGradientBoostingRegressor        0.07
142.7s 579 GammaRegressor                       0.01
142.7s 580 LGBMRegressor                        0.04
142.7s 581 GaussianProcessRegressor             0.01
142.7s 582 ElasticNetCV                         0.06
142.7s 583 BayesianRidge                        0.01
142.7s 584 DummyRegressor                       0.01
142.7s 585 NuSVR                                0.01
142.7s 586 HuberRegressor                       0.02
142.7s 587 SVR                                  0.01
142.7s 588 QuantileRegressor                    0.10
142.7s 589 KernelRidge                          0.01
142.7s 590 PassiveAggressiveRegressor           0.01
142.7s 591 LinearSVR                            0.01
142.7s 592 MLPRegressor                         0.12
142.7s 593 LEARNING RATE: 0.1
142.7s 594 0%|          | 0/42 [00:00<?, ?it/s]  5%|▍         | 2/42 [00:00<00:02, 18.77it/s] 19%|█▉        | 8/42 [00:00<00:00, 40.20it/s] 29%|██▊       | 12/42 [00:00<00:01, 25.65it/s] 36%|███▌      | 15/42 [00:00<00:01, 26.54it/s] 48%|████▊     | 20/42 [00:00<00:00, 31.87it/s] 62%|██████▏   | 26/42 [00:00<00:00, 30.89it/s] 76%|███████▌  | 32/42 [00:01<00:00, 32.09it/s] 86%|████████▌ | 36/42 [00:01<00:00, 26.02it/s] 98%|█████████▊| 41/42 [00:01<00:00, 18.27it/s]100%|██████████| 42/42 [00:01<00:00, 23.76it/s]
142.7s 595 Better model found at epoch 0 with _rmse value: 983235200.0.
142.7s 596 No improvement since epoch 0: early stopping
143.3s 597 XGBoost Predictions vs Actual==========
143.3s 598 actual     predicted
143.3s 599 0  477933632.00  486206368.00
143.3s 600 1  729169472.00  707510912.00
143.3s 601 2  596107456.00  634084352.00
143.3s 602 3 1154638720.00 1138368384.00
143.3s 603 4 1117415168.00 1136631168.00
143.3s 604 XGBoost RMSE:  21789300.0
143.6s 605 Target Variable: Inflation, consumer prices (annual %)
143.6s 606 CATS=====================
143.6s 607 []
143.6s 608 CONTS=====================
143.6s 609 ['GDP (current US$) ', ' GDP per capita (current US$) ', 'GDP growth (annual %)', 'Imports of goods and services (% of GDP)', 'Exports of goods and services (% of GDP)', ' Total reserves (includes gold, current US$) ', 'Population, total', 'Population growth (annual %)', 'Life expectancy at birth, total (years)']
143.6s 610 9
143.6s 611 Looping through continuous variables to find breakpoint
143.6s 612 Continuous variables that made the cut : ['GDP (current US$) ', ' GDP per capita (current US$) ', 'GDP growth (annual %)', 'Imports of goods and services (% of GDP)', 'Exports of goods and services (% of GDP)', ' Total reserves (includes gold, current US$) ', 'Population, total', 'Population growth (annual %)', 'Life expectancy at birth, total (years)']
143.6s 613 Categorical variables that made the cut : []
143.6s 614 Tabular Object size: 61
143.6s 615 problem with getting one batch of indian-economy-from-1960-to-2020
143.9s 616 {'Model': 'AdaBoostRegressor', 'R-Squared': -0.18261135076591906, 'Adjusted R-Squared': -5.504362429212555, 'RMSE': 6.787162458448979, 'Time taken': 0.07648444175720215}
143.9s 617 {'Model': 'BaggingRegressor', 'R-Squared': -0.5981897544698371, 'Adjusted R-Squared': -7.790043649584105, 'RMSE': 7.890079773590716, 'Time taken': 0.02682948112487793}
143.9s 618 {'Model': 'BayesianRidge', 'R-Squared': -0.10574913820819898, 'Adjusted R-Squared': -5.081620260145094, 'RMSE': 6.562896086206177, 'Time taken': 0.012306451797485352}
143.9s 619 {'Model': 'DecisionTreeRegressor', 'R-Squared': -1.885973524551893, 'Adjusted R-Squared': -14.872854385035412, 'RMSE': 10.602624832507528, 'Time taken': 0.009359121322631836}
143.9s 620 {'Model': 'DummyRegressor', 'R-Squared': -0.0764048465949656, 'Adjusted R-Squared': -4.920226656272311, 'RMSE': 6.4752274, 'Time taken': 0.008640289306640625}
143.9s 621 {'Model': 'ElasticNet', 'R-Squared': -0.11339564407204827, 'Adjusted R-Squared': -5.123676042396266, 'RMSE': 6.5855484, 'Time taken': 0.009546518325805664}
143.9s 622 {'Model': 'ElasticNetCV', 'R-Squared': -0.13714127995581316, 'Adjusted R-Squared': -5.254277039756972, 'RMSE': 6.655404, 'Time taken': 0.09391212463378906}
143.9s 623 {'Model': 'ExtraTreeRegressor', 'R-Squared': -2.1239202465532214, 'Adjusted R-Squared': -16.181561356042717, 'RMSE': 11.031058608913627, 'Time taken': 0.010455846786499023}
144.2s 624 {'Model': 'ExtraTreesRegressor', 'R-Squared': -0.29553194836342445, 'Adjusted R-Squared': -6.125425715998834, 'RMSE': 7.103809175454928, 'Time taken': 0.10930752754211426}
144.2s 625 {'Model': 'GammaRegressor', 'R-Squared': -0.14934458283238095, 'Adjusted R-Squared': -5.321395205578095, 'RMSE': 6.691020334374017, 'Time taken': 0.012622833251953125}
144.2s 626 {'Model': 'GaussianProcessRegressor', 'R-Squared': -3.9758338241202456, 'Adjusted R-Squared': -26.36708603266135, 'RMSE': 13.921952802401892, 'Time taken': 0.01485443115234375}
144.2s 627 {'Model': 'GradientBoostingRegressor', 'R-Squared': -0.4500425422485561, 'Adjusted R-Squared': -6.975233982367058, 'RMSE': 7.515495085195642, 'Time taken': 0.0836482048034668}
144.2s 628 {'Model': 'HistGradientBoostingRegressor', 'R-Squared': -0.15068085103491846, 'Adjusted R-Squared': -5.3287446806920515, 'RMSE': 6.694908811589353, 'Time taken': 0.07839441299438477}
144.4s 629 {'Model': 'HuberRegressor', 'R-Squared': 0.0008419871935244627, 'Adjusted R-Squared': -4.495369070435616, 'RMSE': 6.238559347709263, 'Time taken': 0.03916287422180176}
144.4s 630 {'Model': 'KNeighborsRegressor', 'R-Squared': -0.2580784953681219, 'Adjusted R-Squared': -5.919431724524671, 'RMSE': 7.000372, 'Time taken': 0.01026153564453125}
144.4s 631 {'Model': 'KernelRidge', 'R-Squared': -0.9598083237612298, 'Adjusted R-Squared': -9.778945780686763, 'RMSE': 8.737235, 'Time taken': 0.009583234786987305}
144.4s 632 {'Model': 'Lars', 'R-Squared': -0.10015859143929573, 'Adjusted R-Squared': -5.050872252916126, 'RMSE': 6.546284, 'Time taken': 0.011197566986083984}
144.4s 633 {'Model': 'LarsCV', 'R-Squared': -0.13679219676197918, 'Adjusted R-Squared': -5.252357082190885, 'RMSE': 6.654382, 'Time taken': 0.02295660972595215}
144.4s 634 {'Model': 'Lasso', 'R-Squared': -0.08304925805353136, 'Adjusted R-Squared': -4.9567709192944225, 'RMSE': 6.495182, 'Time taken': 0.009853363037109375}
144.7s 635 {'Model': 'LassoCV', 'R-Squared': -0.1370159507416442, 'Adjusted R-Squared': -5.253587729079043, 'RMSE': 6.6550374, 'Time taken': 0.16731643676757812}
144.7s 636 {'Model': 'LassoLars', 'R-Squared': -0.0764048465949656, 'Adjusted R-Squared': -4.920226656272311, 'RMSE': 6.4752274, 'Time taken': 0.01063847541809082}
144.7s 637 {'Model': 'LassoLarsCV', 'R-Squared': -0.1320336444706769, 'Adjusted R-Squared': -5.226185044588723, 'RMSE': 6.640441, 'Time taken': 0.02621293067932129}
144.7s 638 {'Model': 'LassoLarsIC', 'R-Squared': -0.15488864081406772, 'Adjusted R-Squared': -5.351887524477372, 'RMSE': 6.707139, 'Time taken': 0.01329803466796875}
144.7s 639 {'Model': 'LinearRegression', 'R-Squared': -0.10499376040450525, 'Adjusted R-Squared': -5.077465682224779, 'RMSE': 6.5606546, 'Time taken': 0.012646913528442383}
144.7s 640 {'Model': 'LinearSVR', 'R-Squared': -0.03631508938994066, 'Adjusted R-Squared': -4.699732991644674, 'RMSE': 6.353501459384508, 'Time taken': 0.01086115837097168}
144.9s 641 {'Model': 'MLPRegressor', 'R-Squared': -0.16647820760888865, 'Adjusted R-Squared': -5.4156301418488875, 'RMSE': 6.7407084, 'Time taken': 0.13898754119873047}
144.9s 642 {'Model': 'NuSVR', 'R-Squared': -0.05718194787921593, 'Adjusted R-Squared': -4.814500713335688, 'RMSE': 6.41714854386146, 'Time taken': 0.01820206642150879}
144.9s 643 {'Model': 'OrthogonalMatchingPursuit', 'R-Squared': -0.17995603410074423, 'Adjusted R-Squared': -5.489758187554093, 'RMSE': 6.7795385703558555, 'Time taken': 0.013692617416381836}
144.9s 644 {'Model': 'OrthogonalMatchingPursuitCV', 'R-Squared': -0.17995603410074423, 'Adjusted R-Squared': -5.489758187554093, 'RMSE': 6.7795385703558555, 'Time taken': 0.021394729614257812}
144.9s 645 {'Model': 'PassiveAggressiveRegressor', 'R-Squared': -1.5092852774135337, 'Adjusted R-Squared': -12.801069025774435, 'RMSE': 9.886492525755886, 'Time taken': 0.010505437850952148}
144.9s 646 {'Model': 'PoissonRegressor', 'R-Squared': -0.14194570760336056, 'Adjusted R-Squared': -5.280701391818483, 'RMSE': 6.669448929129903, 'Time taken': 0.012714862823486328}
144.9s 647 {'Model': 'QuantileRegressor', 'R-Squared': -0.010597709496044772, 'Adjusted R-Squared': -4.558287402228246, 'RMSE': 6.274171388080176, 'Time taken': 0.08417963981628418}
145.2s 648 {'Model': 'RANSACRegressor', 'R-Squared': -0.014917122805235605, 'Adjusted R-Squared': -4.582044175428796, 'RMSE': 6.2875657, 'Time taken': 0.12382841110229492}
145.2s 649 {'Model': 'RandomForestRegressor', 'R-Squared': -0.37288460575111815, 'Adjusted R-Squared': -6.55086533163115, 'RMSE': 7.3128091738678425, 'Time taken': 0.1435706615447998}
145.2s 650 {'Model': 'Ridge', 'R-Squared': -0.11969034724277727, 'Adjusted R-Squared': -5.158296909835275, 'RMSE': 6.604139, 'Time taken': 0.01029348373413086}
145.2s 651 {'Model': 'RidgeCV', 'R-Squared': -0.11969054814847757, 'Adjusted R-Squared': -5.158298014816626, 'RMSE': 6.604139360745634, 'Time taken': 0.01232290267944336}
145.2s 652 {'Model': 'SGDRegressor', 'R-Squared': -0.14127711931190845, 'Adjusted R-Squared': -5.2770241562154965, 'RMSE': 6.667496223187537, 'Time taken': 0.01030421257019043}
145.2s 653 {'Model': 'SVR', 'R-Squared': -0.04022438495330083, 'Adjusted R-Squared': -4.721234117243155, 'RMSE': 6.365473848643853, 'Time taken': 0.009804725646972656}
145.2s 654 {'Model': 'TransformedTargetRegressor', 'R-Squared': -0.10499376040450525, 'Adjusted R-Squared': -5.077465682224779, 'RMSE': 6.5606546, 'Time taken': 0.009929418563842773}
145.4s 655 {'Model': 'TweedieRegressor', 'R-Squared': -0.14876437951708965, 'Adjusted R-Squared': -5.318204087343993, 'RMSE': 6.6893312664034745, 'Time taken': 0.014209270477294922}
145.7s 656 {'Model': 'XGBRegressor', 'R-Squared': -0.18920237994956124, 'Adjusted R-Squared': -5.540613089722587, 'RMSE': 6.80605, 'Time taken': 0.3761570453643799}
145.7s 657 {'Model': 'LGBMRegressor', 'R-Squared': -0.16499139987262978, 'Adjusted R-Squared': -5.407452699299464, 'RMSE': 6.736411099891504, 'Time taken': 0.03722429275512695}
145.7s 658 Project: indian-economy-from-1960-to-2020
145.7s 659 indian-economy-from-1960-to-2020
145.7s 660 Target: Inflation, consumer prices (annual %)
145.7s 661 Inflation, consumer prices (annual %)
145.7s 662 Target Standard Deviation: 4.445106029510498
145.7s 663 Adjusted R-Squared  R-Squared  RMSE  Time Taken
145.7s 664 Model
145.7s 665 HuberRegressor                              -4.50       0.00  6.24        0.04
145.7s 666 QuantileRegressor                           -4.56      -0.01  6.27        0.08
145.7s 667 RANSACRegressor                             -4.58      -0.01  6.29        0.12
145.7s 668 LinearSVR                                   -4.70      -0.04  6.35        0.01
145.7s 669 SVR                                         -4.72      -0.04  6.37        0.01
145.7s 670 NuSVR                                       -4.81      -0.06  6.42        0.02
145.7s 671 DummyRegressor                              -4.92      -0.08  6.48        0.01
145.7s 672 LassoLars                                   -4.92      -0.08  6.48        0.01
145.7s 673 Lasso                                       -4.96      -0.08  6.50        0.01
145.7s 674 Lars                                        -5.05      -0.10  6.55        0.01
145.7s 675 LinearRegression                            -5.08      -0.10  6.56        0.01
145.7s 676 TransformedTargetRegressor                  -5.08      -0.10  6.56        0.01
145.7s 677 BayesianRidge                               -5.08      -0.11  6.56        0.01
145.7s 678 ElasticNet                                  -5.12      -0.11  6.59        0.01
145.7s 679 Ridge                                       -5.16      -0.12  6.60        0.01
145.7s 680 RidgeCV                                     -5.16      -0.12  6.60        0.01
145.7s 681 LassoLarsCV                                 -5.23      -0.13  6.64        0.03
145.7s 682 LarsCV                                      -5.25      -0.14  6.65        0.02
145.7s 683 LassoCV                                     -5.25      -0.14  6.66        0.17
145.7s 684 ElasticNetCV                                -5.25      -0.14  6.66        0.09
145.7s 685 SGDRegressor                                -5.28      -0.14  6.67        0.01
145.7s 686 PoissonRegressor                            -5.28      -0.14  6.67        0.01
145.7s 687 TweedieRegressor                            -5.32      -0.15  6.69        0.01
145.7s 688 GammaRegressor                              -5.32      -0.15  6.69        0.01
145.7s 689 HistGradientBoostingRegressor               -5.33      -0.15  6.69        0.08
145.7s 690 LassoLarsIC                                 -5.35      -0.15  6.71        0.01
145.7s 691 LGBMRegressor                               -5.41      -0.16  6.74        0.04
145.7s 692 MLPRegressor                                -5.42      -0.17  6.74        0.14
145.7s 693 OrthogonalMatchingPursuit                   -5.49      -0.18  6.78        0.01
145.7s 694 OrthogonalMatchingPursuitCV                 -5.49      -0.18  6.78        0.02
145.7s 695 AdaBoostRegressor                           -5.50      -0.18  6.79        0.08
145.7s 696 XGBRegressor                                -5.54      -0.19  6.81        0.38
145.7s 697 KNeighborsRegressor                         -5.92      -0.26  7.00        0.01
145.7s 698 ExtraTreesRegressor                         -6.13      -0.30  7.10        0.11
145.7s 699 RandomForestRegressor                       -6.55      -0.37  7.31        0.14
145.7s 700 GradientBoostingRegressor                   -6.98      -0.45  7.52        0.08
145.7s 701 BaggingRegressor                            -7.79      -0.60  7.89        0.03
145.7s 702 KernelRidge                                 -9.78      -0.96  8.74        0.01
145.7s 703 PassiveAggressiveRegressor                 -12.80      -1.51  9.89        0.01
145.7s 704 DecisionTreeRegressor                      -14.87      -1.89 10.60        0.01
145.7s 705 ExtraTreeRegressor                         -16.18      -2.12 11.03        0.01
145.7s 706 GaussianProcessRegressor                   -26.37      -3.98 13.92        0.01
145.7s 707 LEARNING RATE: 0.1
145.7s 708 0%|          | 0/42 [00:00<?, ?it/s]  5%|▍         | 2/42 [00:00<00:02, 19.33it/s] 17%|█▋        | 7/42 [00:00<00:01, 30.84it/s] 24%|██▍       | 10/42 [00:00<00:01, 26.81it/s] 31%|███       | 13/42 [00:00<00:01, 22.04it/s] 45%|████▌     | 19/42 [00:00<00:00, 32.09it/s] 55%|█████▍    | 23/42 [00:00<00:00, 25.72it/s] 62%|██████▏   | 26/42 [00:01<00:00, 23.27it/s] 76%|███████▌  | 32/42 [00:01<00:00, 27.61it/s] 83%|████████▎ | 35/42 [00:01<00:00, 20.17it/s] 98%|█████████▊| 41/42 [00:01<00:00, 17.03it/s]100%|██████████| 42/42 [00:01<00:00, 21.48it/s]
145.7s 709 Better model found at epoch 0 with _rmse value: 20.278240203857422.
145.7s 710 No improvement since epoch 0: early stopping
147.2s 711 XGBoost Predictions vs Actual==========
147.2s 712 actual  predicted
147.2s 713 0   13.06       5.03
147.2s 714 1    8.35       6.00
147.2s 715 2   -7.63       5.15
147.2s 716 3    9.48      11.03
147.2s 717 4    6.33       7.23
147.2s 718 XGBoost RMSE:  6.80605
147.5s 719 Target Variable:  Total reserves (includes gold, current US$)
147.5s 720 CATS=====================
147.5s 721 []
147.5s 722 CONTS=====================
147.5s 723 ['GDP (current US$) ', ' GDP per capita (current US$) ', 'GDP growth (annual %)', 'Imports of goods and services (% of GDP)', 'Exports of goods and services (% of GDP)', 'Inflation, consumer prices (annual %)', 'Population, total', 'Population growth (annual %)', 'Life expectancy at birth, total (years)']
147.5s 724 9
147.5s 725 Looping through continuous variables to find breakpoint
147.5s 726 Continuous variables that made the cut : ['GDP (current US$) ', ' GDP per capita (current US$) ', 'GDP growth (annual %)', 'Imports of goods and services (% of GDP)', 'Exports of goods and services (% of GDP)', 'Inflation, consumer prices (annual %)', 'Population, total', 'Population growth (annual %)', 'Life expectancy at birth, total (years)']
147.5s 727 Categorical variables that made the cut : []
147.5s 728 Tabular Object size: 61
147.5s 729 problem with getting one batch of indian-economy-from-1960-to-2020
147.8s 730 {'Model': 'AdaBoostRegressor', 'R-Squared': 0.9174924997182037, 'Adjusted R-Squared': 0.5462087484501202, 'RMSE': 51230032290.06406, 'Time taken': 0.07777976989746094}
147.8s 731 {'Model': 'BaggingRegressor', 'R-Squared': 0.8138055172732171, 'Adjusted R-Squared': -0.024069654997305623, 'RMSE': 76959337206.78256, 'Time taken': 0.02807164192199707}
147.8s 732 {'Model': 'BayesianRidge', 'R-Squared': -0.00010135025336621695, 'Adjusted R-Squared': -4.500557426393514, 'RMSE': 178361009463.401, 'Time taken': 0.012328624725341797}
147.8s 733 {'Model': 'DecisionTreeRegressor', 'R-Squared': 0.7821133552145276, 'Adjusted R-Squared': -0.19837654632009816, 'RMSE': 83251721068.47827, 'Time taken': 0.010061502456665039}
147.8s 734 {'Model': 'DummyRegressor', 'R-Squared': -0.00010137949813149305, 'Adjusted R-Squared': -4.500557587239723, 'RMSE': 178361000000.0, 'Time taken': 0.008860111236572266}
147.8s 735 {'Model': 'ElasticNet', 'R-Squared': 0.8240424171038213, 'Adjusted R-Squared': 0.03223329407101727, 'RMSE': 74813830000.0, 'Time taken': 0.01105642318725586}
147.8s 736 {'Model': 'ElasticNetCV', 'R-Squared': -0.00010137949813149305, 'Adjusted R-Squared': -4.500557587239723, 'RMSE': 178361000000.0, 'Time taken': 0.05728030204772949}
147.8s 737 {'Model': 'ExtraTreeRegressor', 'R-Squared': 0.8510790875312683, 'Adjusted R-Squared': 0.1809349814219754, 'RMSE': 68826511721.53452, 'Time taken': 0.011680364608764648}
148.1s 738 {'Model': 'ExtraTreesRegressor', 'R-Squared': 0.9002317555204338, 'Adjusted R-Squared': 0.45127465536238576, 'RMSE': 56334452782.574394, 'Time taken': 0.10913419723510742}
148.1s 739 {'Model': 'GammaRegressor', 'R-Squared': 0.7013510201833718, 'Adjusted R-Squared': -0.642569388991455, 'RMSE': 97467187118.2796, 'Time taken': 0.013523340225219727}
148.1s 740 {'Model': 'GaussianProcessRegressor', 'R-Squared': 0.08642807926590468, 'Adjusted R-Squared': -4.024645564037524, 'RMSE': 170470520116.22504, 'Time taken': 0.013161659240722656}
148.1s 741 {'Model': 'GradientBoostingRegressor', 'R-Squared': 0.8948124200587163, 'Adjusted R-Squared': 0.42146831032293974, 'RMSE': 57844243616.677635, 'Time taken': 0.08550596237182617}
148.3s 742 {'Model': 'HistGradientBoostingRegressor', 'R-Squared': 0.393816345579205, 'Adjusted R-Squared': -2.334010099314373, 'RMSE': 138860915950.2978, 'Time taken': 0.09888815879821777}
148.3s 743 {'Model': 'HuberRegressor', 'R-Squared': -0.31101391658091915, 'Adjusted R-Squared': -6.2105765411950555, 'RMSE': 204212144366.48096, 'Time taken': 0.012546300888061523}
148.3s 744 {'Model': 'KNeighborsRegressor', 'R-Squared': 0.8570076746604143, 'Adjusted R-Squared': 0.21354221063227852, 'RMSE': 67442594000.0, 'Time taken': 0.010250329971313477}
148.3s 745 {'Model': 'KernelRidge', 'R-Squared': 0.5532041958497537, 'Adjusted R-Squared': -1.457376922826355, 'RMSE': 119215420000.0, 'Time taken': 0.010185718536376953}
148.3s 746 {'Model': 'Lars', 'R-Squared': -0.3849019162268892, 'Adjusted R-Squared': -6.6169605392478905, 'RMSE': 209887900000.0, 'Time taken': 0.010880708694458008}
148.3s 747 {'Model': 'LarsCV', 'R-Squared': 0.8157424957260484, 'Adjusted R-Squared': -0.0134162735067338, 'RMSE': 76557990000.0, 'Time taken': 0.02273273468017578}
148.3s 748 {'Model': 'Lasso', 'R-Squared': 0.9082750529466355, 'Adjusted R-Squared': 0.49551279120649505, 'RMSE': 54015900000.0, 'Time taken': 0.011163949966430664}
148.3s 749 {'Model': 'LassoCV', 'R-Squared': 0.9128830870547031, 'Adjusted R-Squared': 0.5208569788008671, 'RMSE': 52641608000.0, 'Time taken': 0.07938623428344727}
148.3s 750 {'Model': 'LassoLars', 'R-Squared': 0.9025961332822048, 'Adjusted R-Squared': 0.4642787330521263, 'RMSE': 55662924000.0, 'Time taken': 0.014992237091064453}
148.5s 751 {'Model': 'LassoLarsCV', 'R-Squared': 0.9025959652703849, 'Adjusted R-Squared': 0.4642778089871169, 'RMSE': 55662970000.0, 'Time taken': 0.03791332244873047}
148.5s 752 {'Model': 'LassoLarsIC', 'R-Squared': 0.904448283637933, 'Adjusted R-Squared': 0.47446556000863116, 'RMSE': 55131160000.0, 'Time taken': 0.01660013198852539}
148.5s 753 {'Model': 'LinearRegression', 'R-Squared': 0.9026020517648593, 'Adjusted R-Squared': 0.4643112847067261, 'RMSE': 55661232000.0, 'Time taken': 0.009876489639282227}
148.5s 754 {'Model': 'LinearSVR', 'R-Squared': -0.31101391710185844, 'Adjusted R-Squared': -6.210576544060221, 'RMSE': 204212144407.05344, 'Time taken': 0.009473085403442383}
148.5s 755 {'Model': 'MLPRegressor', 'R-Squared': -0.31101389508770416, 'Adjusted R-Squared': -6.210576422982373, 'RMSE': 204212140000.0, 'Time taken': 0.04614853858947754}
148.5s 756 {'Model': 'NuSVR', 'R-Squared': -0.0027057165008885775, 'Adjusted R-Squared': -4.514881440754888, 'RMSE': 178593093628.27826, 'Time taken': 0.011373043060302734}
148.5s 757 {'Model': 'OrthogonalMatchingPursuit', 'R-Squared': 0.9148912508759428, 'Adjusted R-Squared': 0.5319018798176854, 'RMSE': 52031340944.52291, 'Time taken': 0.009784460067749023}
148.5s 758 {'Model': 'OrthogonalMatchingPursuitCV', 'R-Squared': 0.8841661380167541, 'Adjusted R-Squared': 0.36291375909214785, 'RMSE': 60700977243.21933, 'Time taken': 0.015449762344360352}
148.5s 759 {'Model': 'PassiveAggressiveRegressor', 'R-Squared': -0.31101361097357483, 'Adjusted R-Squared': -6.2105748603546616, 'RMSE': 204212120564.7753, 'Time taken': 0.013173103332519531}
148.5s 760 {'Model': 'PoissonRegressor', 'R-Squared': 0.747820049318683, 'Adjusted R-Squared': -0.3869897287472437, 'RMSE': 89563940457.70995, 'Time taken': 0.02426934242248535}
148.5s 761 {'Model': 'QuantileRegressor', 'R-Squared': -0.3110129750313797, 'Adjusted R-Squared': -6.210571362672589, 'RMSE': 204212071035.49545, 'Time taken': 0.025051116943359375}
148.8s 762 {'Model': 'RANSACRegressor', 'R-Squared': 0.9647432741014991, 'Adjusted R-Squared': 0.8060880075582448, 'RMSE': 33488749000.0, 'Time taken': 0.12815093994140625}
148.8s 763 {'Model': 'RandomForestRegressor', 'R-Squared': 0.8903150890549167, 'Adjusted R-Squared': 0.3967329898020421, 'RMSE': 59067876519.00497, 'Time taken': 0.14445233345031738}
148.8s 764 {'Model': 'Ridge', 'R-Squared': 0.9087137151270684, 'Adjusted R-Squared': 0.4979254331988765, 'RMSE': 53886587000.0, 'Time taken': 0.010404109954833984}
148.8s 765 {'Model': 'RidgeCV', 'R-Squared': 0.9105069701545011, 'Adjusted R-Squared': 0.5077883358497561, 'RMSE': 53354680139.56536, 'Time taken': 0.009710550308227539}
148.8s 766 {'Model': 'SGDRegressor', 'R-Squared': 0.9129012140585333, 'Adjusted R-Squared': 0.5209566773219332, 'RMSE': 52636131782.02481, 'Time taken': 0.010128498077392578}
148.8s 767 {'Model': 'SVR', 'R-Squared': -0.24318819425951976, 'Adjusted R-Squared': -5.837535068427359, 'RMSE': 198859504738.9218, 'Time taken': 0.00960540771484375}
148.8s 768 {'Model': 'TransformedTargetRegressor', 'R-Squared': 0.9026020517648593, 'Adjusted R-Squared': 0.4643112847067261, 'RMSE': 55661232000.0, 'Time taken': 0.009704828262329102}
149.0s 769 {'Model': 'TweedieRegressor', 'R-Squared': 0.7662386742148056, 'Adjusted R-Squared': -0.2856872918185691, 'RMSE': 86231163440.35738, 'Time taken': 0.016571998596191406}
149.3s 770 {'Model': 'XGBRegressor', 'R-Squared': 0.9132133184186866, 'Adjusted R-Squared': 0.5226732513027762, 'RMSE': 52541740000.0, 'Time taken': 0.3951113224029541}
149.3s 771 {'Model': 'LGBMRegressor', 'R-Squared': 0.2968685147389106, 'Adjusted R-Squared': -2.8672231689359915, 'RMSE': 149553364423.78806, 'Time taken': 0.022443771362304688}
149.3s 772 Project: indian-economy-from-1960-to-2020
149.3s 773 indian-economy-from-1960-to-2020
149.3s 774 Target:  Total reserves (includes gold, current US$)
149.3s 775 Total reserves (includes gold, current US$)
149.3s 776 Target Standard Deviation: 140192595968.0
149.3s 777 Adjusted R-Squared  R-Squared            RMSE  \
149.3s 778 Model
149.3s 779 RANSACRegressor                              0.81       0.96  33488748544.00
149.3s 780 AdaBoostRegressor                            0.55       0.92  51230032290.06
149.3s 781 OrthogonalMatchingPursuit                    0.53       0.91  52031340944.52
149.3s 782 XGBRegressor                                 0.52       0.91  52541739008.00
149.3s 783 SGDRegressor                                 0.52       0.91  52636131782.02
149.3s 784 LassoCV                                      0.52       0.91  52641607680.00
149.3s 785 RidgeCV                                      0.51       0.91  53354680139.57
149.3s 786 Ridge                                        0.50       0.91  53886586880.00
149.3s 787 Lasso                                        0.50       0.91  54015901696.00
149.3s 788 LassoLarsIC                                  0.47       0.90  55131160576.00
149.3s 789 TransformedTargetRegressor                   0.46       0.90  55661232128.00
149.3s 790 LinearRegression                             0.46       0.90  55661232128.00
149.3s 791 LassoLars                                    0.46       0.90  55662923776.00
149.3s 792 LassoLarsCV                                  0.46       0.90  55662968832.00
149.3s 793 ExtraTreesRegressor                          0.45       0.90  56334452782.57
149.3s 794 GradientBoostingRegressor                    0.42       0.89  57844243616.68
149.3s 795 RandomForestRegressor                        0.40       0.89  59067876519.00
149.3s 796 OrthogonalMatchingPursuitCV                  0.36       0.88  60700977243.22
149.3s 797 KNeighborsRegressor                          0.21       0.86  67442593792.00
149.3s 798 ExtraTreeRegressor                           0.18       0.85  68826511721.53
149.3s 799 ElasticNet                                   0.03       0.82  74813833216.00
149.3s 800 LarsCV                                      -0.01       0.82  76557991936.00
149.3s 801 BaggingRegressor                            -0.02       0.81  76959337206.78
149.3s 802 DecisionTreeRegressor                       -0.20       0.78  83251721068.48
149.3s 803 TweedieRegressor                            -0.29       0.77  86231163440.36
149.3s 804 PoissonRegressor                            -0.39       0.75  89563940457.71
149.3s 805 GammaRegressor                              -0.64       0.70  97467187118.28
149.3s 806 KernelRidge                                 -1.46       0.55 119215423488.00
149.3s 807 HistGradientBoostingRegressor               -2.33       0.39 138860915950.30
149.3s 808 LGBMRegressor                               -2.87       0.30 149553364423.79
149.3s 809 GaussianProcessRegressor                    -4.02       0.09 170470520116.23
149.3s 810 BayesianRidge                               -4.50      -0.00 178361009463.40
149.3s 811 ElasticNetCV                                -4.50      -0.00 178361008128.00
149.3s 812 DummyRegressor                              -4.50      -0.00 178361008128.00
149.3s 813 NuSVR                                       -4.51      -0.00 178593093628.28
149.3s 814 SVR                                         -5.84      -0.24 198859504738.92
149.3s 815 QuantileRegressor                           -6.21      -0.31 204212071035.50
149.3s 816 PassiveAggressiveRegressor                  -6.21      -0.31 204212120564.78
149.3s 817 MLPRegressor                                -6.21      -0.31 204212142080.00
149.3s 818 HuberRegressor                              -6.21      -0.31 204212144366.48
149.3s 819 LinearSVR                                   -6.21      -0.31 204212144407.05
149.3s 820 Lars                                        -6.62      -0.38 209887903744.00
149.3s 821 
149.3s 822 Time Taken
149.3s 823 Model
149.3s 824 RANSACRegressor                      0.13
149.3s 825 AdaBoostRegressor                    0.08
149.3s 826 OrthogonalMatchingPursuit            0.01
149.3s 827 XGBRegressor                         0.40
149.3s 828 SGDRegressor                         0.01
149.3s 829 LassoCV                              0.08
149.3s 830 RidgeCV                              0.01
149.3s 831 Ridge                                0.01
149.3s 832 Lasso                                0.01
149.3s 833 LassoLarsIC                          0.02
149.3s 834 TransformedTargetRegressor           0.01
149.3s 835 LinearRegression                     0.01
149.3s 836 LassoLars                            0.01
149.3s 837 LassoLarsCV                          0.04
149.3s 838 ExtraTreesRegressor                  0.11
149.3s 839 GradientBoostingRegressor            0.09
149.3s 840 RandomForestRegressor                0.14
149.3s 841 OrthogonalMatchingPursuitCV          0.02
149.3s 842 KNeighborsRegressor                  0.01
149.3s 843 ExtraTreeRegressor                   0.01
149.3s 844 ElasticNet                           0.01
149.3s 845 LarsCV                               0.02
149.3s 846 BaggingRegressor                     0.03
149.3s 847 DecisionTreeRegressor                0.01
149.3s 848 TweedieRegressor                     0.02
149.3s 849 PoissonRegressor                     0.02
149.3s 850 GammaRegressor                       0.01
149.3s 851 KernelRidge                          0.01
149.3s 852 HistGradientBoostingRegressor        0.10
149.3s 853 LGBMRegressor                        0.02
149.3s 854 GaussianProcessRegressor             0.01
149.3s 855 BayesianRidge                        0.01
149.3s 856 ElasticNetCV                         0.06
149.3s 857 DummyRegressor                       0.01
149.3s 858 NuSVR                                0.01
149.3s 859 SVR                                  0.01
149.3s 860 QuantileRegressor                    0.03
149.3s 861 PassiveAggressiveRegressor           0.01
149.3s 862 MLPRegressor                         0.05
149.3s 863 HuberRegressor                       0.01
149.3s 864 LinearSVR                            0.01
149.3s 865 Lars                                 0.01
149.3s 866 LEARNING RATE: 0.1
149.3s 867 0%|          | 0/42 [00:00<?, ?it/s]  5%|▍         | 2/42 [00:00<00:02, 18.86it/s] 17%|█▋        | 7/42 [00:00<00:00, 36.53it/s] 26%|██▌       | 11/42 [00:00<00:00, 31.21it/s] 36%|███▌      | 15/42 [00:00<00:01, 24.83it/s] 48%|████▊     | 20/42 [00:00<00:00, 28.74it/s] 62%|██████▏   | 26/42 [00:00<00:00, 33.57it/s] 76%|███████▌  | 32/42 [00:00<00:00, 40.11it/s] 88%|████████▊ | 37/42 [00:01<00:00, 27.71it/s] 98%|█████████▊| 41/42 [00:01<00:00, 18.23it/s]100%|██████████| 42/42 [00:01<00:00, 24.64it/s]
149.3s 868 Better model found at epoch 0 with _rmse value: 204212142080.0.
149.4s 869 No improvement since epoch 0: early stopping
149.9s 870 XGBoost Predictions vs Actual==========
149.9s 871 actual       predicted
149.9s 872 0  22864635904.00  24884035584.00
149.9s 873 1 361694330880.00 361389588480.00
149.9s 874 2  24220928000.00  11754714112.00
149.9s 875 3 590227374080.00 409106350080.00
149.9s 876 4   1023173248.00    927529472.00
149.9s 877 XGBoost RMSE:  52541740000.0
150.3s 878 Target Variable: Exports of goods and services (% of GDP)
150.3s 879 CATS=====================
150.3s 880 []
150.3s 881 CONTS=====================
150.3s 882 ['GDP (current US$) ', ' GDP per capita (current US$) ', 'GDP growth (annual %)', 'Imports of goods and services (% of GDP)', ' Total reserves (includes gold, current US$) ', 'Inflation, consumer prices (annual %)', 'Population, total', 'Population growth (annual %)', 'Life expectancy at birth, total (years)']
150.3s 883 9
150.3s 884 Looping through continuous variables to find breakpoint
150.3s 885 Continuous variables that made the cut : ['GDP (current US$) ', ' GDP per capita (current US$) ', 'GDP growth (annual %)', 'Imports of goods and services (% of GDP)', ' Total reserves (includes gold, current US$) ', 'Inflation, consumer prices (annual %)', 'Population, total', 'Population growth (annual %)', 'Life expectancy at birth, total (years)']
150.3s 886 Categorical variables that made the cut : []
150.3s 887 Tabular Object size: 61
150.3s 888 problem with getting one batch of indian-economy-from-1960-to-2020
150.6s 889 {'Model': 'AdaBoostRegressor', 'R-Squared': 0.9929700032302159, 'Adjusted R-Squared': 0.9613350177661875, 'RMSE': 0.5985454571108733, 'Time taken': 0.07793760299682617}
150.6s 890 {'Model': 'BaggingRegressor', 'R-Squared': 0.9927405345349413, 'Adjusted R-Squared': 0.960072939942177, 'RMSE': 0.6082356870585245, 'Time taken': 0.027860403060913086}
150.6s 891 {'Model': 'BayesianRidge', 'R-Squared': 0.9917840756149319, 'Adjusted R-Squared': 0.9548124158821253, 'RMSE': 0.6470648266833215, 'Time taken': 0.012309551239013672}
150.6s 892 {'Model': 'DecisionTreeRegressor', 'R-Squared': 0.9753727225427526, 'Adjusted R-Squared': 0.8645499739851396, 'RMSE': 1.1202830828038381, 'Time taken': 0.009768486022949219}
150.6s 893 {'Model': 'DummyRegressor', 'R-Squared': -0.040375237426134136, 'Adjusted R-Squared': -4.722063805843738, 'RMSE': 7.281395, 'Time taken': 0.009255409240722656}
150.6s 894 {'Model': 'ElasticNet', 'R-Squared': 0.904434186695998, 'Adjusted R-Squared': 0.47438802682798875, 'RMSE': 2.20684, 'Time taken': 0.010170221328735352}
150.6s 895 {'Model': 'ElasticNetCV', 'R-Squared': 0.9929599555612065, 'Adjusted R-Squared': 0.9612797555866359, 'RMSE': 0.59897304, 'Time taken': 0.06254434585571289}
150.6s 896 {'Model': 'ExtraTreeRegressor', 'R-Squared': 0.994384936768236, 'Adjusted R-Squared': 0.9691171522252982, 'RMSE': 0.5349299348129636, 'Time taken': 0.011924982070922852}
150.8s 897 {'Model': 'ExtraTreesRegressor', 'R-Squared': 0.9972555786163391, 'Adjusted R-Squared': 0.9849056823898649, 'RMSE': 0.3739770689071639, 'Time taken': 0.11040449142456055}
150.8s 898 {'Model': 'GammaRegressor', 'R-Squared': 0.8567076112406558, 'Adjusted R-Squared': 0.21189186182360664, 'RMSE': 2.702284918911904, 'Time taken': 0.013381719589233398}
150.8s 899 {'Model': 'GaussianProcessRegressor', 'R-Squared': 0.9884499345908594, 'Adjusted R-Squared': 0.9364746402497266, 'RMSE': 0.7672056597700925, 'Time taken': 0.01223134994506836}
150.8s 900 {'Model': 'GradientBoostingRegressor', 'R-Squared': 0.9906795177334806, 'Adjusted R-Squared': 0.9487373475341434, 'RMSE': 0.6891896843875874, 'Time taken': 0.08501768112182617}
150.8s 901 {'Model': 'HistGradientBoostingRegressor', 'R-Squared': 0.9194860864835682, 'Adjusted R-Squared': 0.5571734756596252, 'RMSE': 2.025606325614626, 'Time taken': 0.05544424057006836}
150.8s 902 {'Model': 'HuberRegressor', 'R-Squared': 0.9910659401052764, 'Adjusted R-Squared': 0.9508626705790201, 'RMSE': 0.6747517289145121, 'Time taken': 0.0356442928314209}
151.0s 903 {'Model': 'KNeighborsRegressor', 'R-Squared': 0.958739773949414, 'Adjusted R-Squared': 0.7730687567217771, 'RMSE': 1.4500581, 'Time taken': 0.010977745056152344}
151.0s 904 {'Model': 'KernelRidge', 'R-Squared': -1.4124254357019725, 'Adjusted R-Squared': -12.26833989636085, 'RMSE': 11.087829, 'Time taken': 0.009621381759643555}
151.0s 905 {'Model': 'Lars', 'R-Squared': 0.8769153763404411, 'Adjusted R-Squared': 0.3230345698724263, 'RMSE': 2.5045023, 'Time taken': 0.011338233947753906}
151.0s 906 {'Model': 'LarsCV', 'R-Squared': 0.9858483250422461, 'Adjusted R-Squared': 0.9221657877323534, 'RMSE': 0.8492265, 'Time taken': 0.02268362045288086}
151.0s 907 {'Model': 'Lasso', 'R-Squared': 0.954207108208686, 'Adjusted R-Squared': 0.7481390951477732, 'RMSE': 1.5276315, 'Time taken': 0.009868860244750977}
151.0s 908 {'Model': 'LassoCV', 'R-Squared': 0.9927072475222393, 'Adjusted R-Squared': 0.9598898613723159, 'RMSE': 0.60962856, 'Time taken': 0.060416460037231445}
151.0s 909 {'Model': 'LassoLars', 'R-Squared': -0.040375237426134136, 'Adjusted R-Squared': -4.722063805843738, 'RMSE': 7.281395, 'Time taken': 0.010877370834350586}
151.0s 910 {'Model': 'LassoLarsCV', 'R-Squared': 0.9910138187038579, 'Adjusted R-Squared': 0.9505760028712182, 'RMSE': 0.67671716, 'Time taken': 0.027161836624145508}
151.0s 911 {'Model': 'LassoLarsIC', 'R-Squared': 0.9903780250651503, 'Adjusted R-Squared': 0.9470791378583265, 'RMSE': 0.7002477, 'Time taken': 0.013025045394897461}
151.0s 912 {'Model': 'LinearRegression', 'R-Squared': 0.9901040024862622, 'Adjusted R-Squared': 0.945572013674442, 'RMSE': 0.7101488, 'Time taken': 0.009565591812133789}
151.0s 913 {'Model': 'LinearSVR', 'R-Squared': 0.9935146924083649, 'Adjusted R-Squared': 0.9643308082460068, 'RMSE': 0.5748901474450027, 'Time taken': 0.009370088577270508}
151.3s 914 {'Model': 'MLPRegressor', 'R-Squared': 0.6931690885073232, 'Adjusted R-Squared': -0.6875700132097227, 'RMSE': 3.9542954, 'Time taken': 0.12382388114929199}
151.3s 915 {'Model': 'NuSVR', 'R-Squared': 0.8870221666729301, 'Adjusted R-Squared': 0.37862191670111556, 'RMSE': 2.3994748209579795, 'Time taken': 0.010993003845214844}
151.3s 916 {'Model': 'OrthogonalMatchingPursuit', 'R-Squared': 0.9717749940938801, 'Adjusted R-Squared': 0.8447624675163408, 'RMSE': 1.1993241998206938, 'Time taken': 0.010336637496948242}
151.3s 917 {'Model': 'OrthogonalMatchingPursuitCV', 'R-Squared': 0.9907621215385848, 'Adjusted R-Squared': 0.9491916684622164, 'RMSE': 0.6861288777028322, 'Time taken': 0.015499591827392578}
151.3s 918 {'Model': 'PassiveAggressiveRegressor', 'R-Squared': 0.9799246712812203, 'Adjusted R-Squared': 0.8895856920467116, 'RMSE': 1.0114651151675198, 'Time taken': 0.009708404541015625}
151.3s 919 {'Model': 'PoissonRegressor', 'R-Squared': 0.9822926327352488, 'Adjusted R-Squared': 0.9026094800438684, 'RMSE': 0.9499408713677964, 'Time taken': 0.013329505920410156}
151.3s 920 {'Model': 'QuantileRegressor', 'R-Squared': -0.03033446436765752, 'Adjusted R-Squared': -4.666839554022117, 'RMSE': 7.24617285411142, 'Time taken': 0.0814969539642334}
151.3s 921 {'Model': 'RANSACRegressor', 'R-Squared': 0.9901040130470151, 'Adjusted R-Squared': 0.9455720717585832, 'RMSE': 0.71014845, 'Time taken': 0.03221845626831055}
151.7s 922 {'Model': 'RandomForestRegressor', 'R-Squared': 0.9946282258376442, 'Adjusted R-Squared': 0.9704552421070431, 'RMSE': 0.5232129072620935, 'Time taken': 0.18486499786376953}
151.7s 923 {'Model': 'Ridge', 'R-Squared': 0.9931060547894662, 'Adjusted R-Squared': 0.9620833013420642, 'RMSE': 0.59272534, 'Time taken': 0.01109170913696289}
151.7s 924 {'Model': 'RidgeCV', 'R-Squared': 0.9920779601550181, 'Adjusted R-Squared': 0.9564287808525997, 'RMSE': 0.6353866524624043, 'Time taken': 0.009818077087402344}
151.7s 925 {'Model': 'SGDRegressor', 'R-Squared': 0.9930854677241123, 'Adjusted R-Squared': 0.9619700724826178, 'RMSE': 0.5936096880518931, 'Time taken': 0.011869192123413086}
151.7s 926 {'Model': 'SVR', 'R-Squared': 0.923877165140396, 'Adjusted R-Squared': 0.5813244082721778, 'RMSE': 1.9695955430092025, 'Time taken': 0.009945392608642578}
151.7s 927 {'Model': 'TransformedTargetRegressor', 'R-Squared': 0.9901040024862622, 'Adjusted R-Squared': 0.945572013674442, 'RMSE': 0.7101488, 'Time taken': 0.010219335556030273}
151.7s 928 {'Model': 'TweedieRegressor', 'R-Squared': 0.8907379737773145, 'Adjusted R-Squared': 0.3990588557752295, 'RMSE': 2.3596859203317178, 'Time taken': 0.010979175567626953}
152.0s 929 {'Model': 'XGBRegressor', 'R-Squared': 0.9826115738496233, 'Adjusted R-Squared': 0.904363656172928, 'RMSE': 0.94134694, 'Time taken': 0.3661174774169922}
152.0s 930 {'Model': 'LGBMRegressor', 'R-Squared': 0.9089900174583185, 'Adjusted R-Squared': 0.49944509602075193, 'RMSE': 2.1535952849314115, 'Time taken': 0.029310226440429688}
152.0s 931 Project: indian-economy-from-1960-to-2020
152.0s 932 indian-economy-from-1960-to-2020
152.0s 933 Target: Exports of goods and services (% of GDP)
152.0s 934 Exports of goods and services (% of GDP)
152.0s 935 Target Standard Deviation: 6.939441204071045
152.0s 936 Adjusted R-Squared  R-Squared  RMSE  Time Taken
152.0s 937 Model
152.0s 938 ExtraTreesRegressor                          0.98       1.00  0.37        0.11
152.0s 939 RandomForestRegressor                        0.97       0.99  0.52        0.18
152.0s 940 ExtraTreeRegressor                           0.97       0.99  0.53        0.01
152.0s 941 LinearSVR                                    0.96       0.99  0.57        0.01
152.0s 942 Ridge                                        0.96       0.99  0.59        0.01
152.0s 943 SGDRegressor                                 0.96       0.99  0.59        0.01
152.0s 944 AdaBoostRegressor                            0.96       0.99  0.60        0.08
152.0s 945 ElasticNetCV                                 0.96       0.99  0.60        0.06
152.0s 946 BaggingRegressor                             0.96       0.99  0.61        0.03
152.0s 947 LassoCV                                      0.96       0.99  0.61        0.06
152.0s 948 RidgeCV                                      0.96       0.99  0.64        0.01
152.0s 949 BayesianRidge                                0.95       0.99  0.65        0.01
152.0s 950 HuberRegressor                               0.95       0.99  0.67        0.04
152.0s 951 LassoLarsCV                                  0.95       0.99  0.68        0.03
152.0s 952 OrthogonalMatchingPursuitCV                  0.95       0.99  0.69        0.02
152.0s 953 GradientBoostingRegressor                    0.95       0.99  0.69        0.09
152.0s 954 LassoLarsIC                                  0.95       0.99  0.70        0.01
152.0s 955 RANSACRegressor                              0.95       0.99  0.71        0.03
152.0s 956 TransformedTargetRegressor                   0.95       0.99  0.71        0.01
152.0s 957 LinearRegression                             0.95       0.99  0.71        0.01
152.0s 958 GaussianProcessRegressor                     0.94       0.99  0.77        0.01
152.0s 959 LarsCV                                       0.92       0.99  0.85        0.02
152.0s 960 XGBRegressor                                 0.90       0.98  0.94        0.37
152.0s 961 PoissonRegressor                             0.90       0.98  0.95        0.01
152.0s 962 PassiveAggressiveRegressor                   0.89       0.98  1.01        0.01
152.0s 963 DecisionTreeRegressor                        0.86       0.98  1.12        0.01
152.0s 964 OrthogonalMatchingPursuit                    0.84       0.97  1.20        0.01
152.0s 965 KNeighborsRegressor                          0.77       0.96  1.45        0.01
152.0s 966 Lasso                                        0.75       0.95  1.53        0.01
152.0s 967 SVR                                          0.58       0.92  1.97        0.01
152.0s 968 HistGradientBoostingRegressor                0.56       0.92  2.03        0.06
152.0s 969 LGBMRegressor                                0.50       0.91  2.15        0.03
152.0s 970 ElasticNet                                   0.47       0.90  2.21        0.01
152.0s 971 TweedieRegressor                             0.40       0.89  2.36        0.01
152.0s 972 NuSVR                                        0.38       0.89  2.40        0.01
152.0s 973 Lars                                         0.32       0.88  2.50        0.01
152.0s 974 GammaRegressor                               0.21       0.86  2.70        0.01
152.0s 975 MLPRegressor                                -0.69       0.69  3.95        0.12
152.0s 976 QuantileRegressor                           -4.67      -0.03  7.25        0.08
152.0s 977 LassoLars                                   -4.72      -0.04  7.28        0.01
152.0s 978 DummyRegressor                              -4.72      -0.04  7.28        0.01
152.0s 979 KernelRidge                                -12.27      -1.41 11.09        0.01
152.0s 980 LEARNING RATE: 0.1
152.0s 981 0%|          | 0/42 [00:00<?, ?it/s]  5%|▍         | 2/42 [00:00<00:02, 18.87it/s] 17%|█▋        | 7/42 [00:00<00:00, 35.62it/s] 26%|██▌       | 11/42 [00:00<00:01, 30.83it/s] 36%|███▌      | 15/42 [00:00<00:01, 25.98it/s] 48%|████▊     | 20/42 [00:00<00:00, 31.22it/s] 62%|██████▏   | 26/42 [00:00<00:00, 30.99it/s] 76%|███████▌  | 32/42 [00:01<00:00, 34.36it/s] 86%|████████▌ | 36/42 [00:01<00:00, 26.84it/s] 98%|█████████▊| 41/42 [00:01<00:00, 19.38it/s]100%|██████████| 42/42 [00:01<00:00, 24.90it/s]
152.1s 982 Better model found at epoch 0 with _rmse value: 38.785011291503906.
152.1s 983 No improvement since epoch 0: early stopping
152.6s 984 XGBoost Predictions vs Actual==========
152.6s 985 actual  predicted
152.6s 986 0    4.14       4.62
152.6s 987 1   10.84       9.90
152.6s 988 2   24.53      24.54
152.6s 989 3    5.60       6.21
152.6s 990 4    5.94       6.04
152.6s 991 XGBoost RMSE:  0.94134694
153.0s 992 Target Variable: Imports of goods and services (% of GDP)
153.0s 993 CATS=====================
153.0s 994 []
153.0s 995 CONTS=====================
153.0s 996 ['GDP (current US$) ', ' GDP per capita (current US$) ', 'GDP growth (annual %)', 'Exports of goods and services (% of GDP)', ' Total reserves (includes gold, current US$) ', 'Inflation, consumer prices (annual %)', 'Population, total', 'Population growth (annual %)', 'Life expectancy at birth, total (years)']
153.0s 997 9
153.0s 998 Looping through continuous variables to find breakpoint
153.0s 999 Continuous variables that made the cut : ['GDP (current US$) ', ' GDP per capita (current US$) ', 'GDP growth (annual %)', 'Exports of goods and services (% of GDP)', ' Total reserves (includes gold, current US$) ', 'Inflation, consumer prices (annual %)', 'Population, total', 'Population growth (annual %)', 'Life expectancy at birth, total (years)']
153.0s 1000 Categorical variables that made the cut : []
153.0s 1001 Tabular Object size: 61
153.0s 1002 problem with getting one batch of indian-economy-from-1960-to-2020
153.3s 1003 {'Model': 'AdaBoostRegressor', 'R-Squared': 0.9640356582301852, 'Adjusted R-Squared': 0.8021961202660187, 'RMSE': 1.8056261880690878, 'Time taken': 0.07968735694885254}
153.3s 1004 {'Model': 'BaggingRegressor', 'R-Squared': 0.9836671393527856, 'Adjusted R-Squared': 0.9101692664403208, 'RMSE': 1.2168104063527057, 'Time taken': 0.027559518814086914}
153.3s 1005 {'Model': 'BayesianRidge', 'R-Squared': 0.9825827762966215, 'Adjusted R-Squared': 0.9042052696314182, 'RMSE': 1.256554274361322, 'Time taken': 0.01208186149597168}
153.3s 1006 {'Model': 'DecisionTreeRegressor', 'R-Squared': 0.8416488842455854, 'Adjusted R-Squared': 0.12906886335071954, 'RMSE': 3.7888058457579423, 'Time taken': 0.009463310241699219}
153.3s 1007 {'Model': 'DummyRegressor', 'R-Squared': -0.09706203813542613, 'Adjusted R-Squared': -5.0338412097448435, 'RMSE': 9.972577, 'Time taken': 0.00871896743774414}
153.3s 1008 {'Model': 'ElasticNet', 'R-Squared': 0.8024272282526184, 'Adjusted R-Squared': -0.086650244610599, 'RMSE': 4.2320943, 'Time taken': 0.00951695442199707}
153.3s 1009 {'Model': 'ElasticNetCV', 'R-Squared': 0.9735535216658908, 'Adjusted R-Squared': 0.8545443691623995, 'RMSE': 1.5483735, 'Time taken': 0.06216764450073242}
153.3s 1010 {'Model': 'ExtraTreeRegressor', 'R-Squared': 0.9713103774139119, 'Adjusted R-Squared': 0.8422070757765154, 'RMSE': 1.6127022966946307, 'Time taken': 0.011273860931396484}
153.5s 1011 {'Model': 'ExtraTreesRegressor', 'R-Squared': 0.9843348173031436, 'Adjusted R-Squared': 0.9138414951672901, 'RMSE': 1.191679638849298, 'Time taken': 0.11391901969909668}
153.5s 1012 {'Model': 'GammaRegressor', 'R-Squared': 0.7664268892331283, 'Adjusted R-Squared': -0.28465210921779427, 'RMSE': 4.60154008147308, 'Time taken': 0.013740777969360352}
153.5s 1013 {'Model': 'GaussianProcessRegressor', 'R-Squared': 0.38317012348170787, 'Adjusted R-Squared': -2.3925643208506067, 'RMSE': 7.477811052603123, 'Time taken': 0.012877225875854492}
153.5s 1014 {'Model': 'GradientBoostingRegressor', 'R-Squared': 0.9598201753675004, 'Adjusted R-Squared': 0.7790109645212523, 'RMSE': 1.9085160006239392, 'Time taken': 0.09058070182800293}
153.5s 1015 {'Model': 'HistGradientBoostingRegressor', 'R-Squared': 0.6576606462902452, 'Adjusted R-Squared': -0.8828664454036512, 'RMSE': 5.5708337766026474, 'Time taken': 0.061428070068359375}
153.7s 1016 {'Model': 'HuberRegressor', 'R-Squared': 0.9923468660295994, 'Adjusted R-Squared': 0.9579077631627968, 'RMSE': 0.8329356391442719, 'Time taken': 0.04020547866821289}
153.7s 1017 {'Model': 'KNeighborsRegressor', 'R-Squared': 0.9362476801153337, 'Adjusted R-Squared': 0.6493622406343351, 'RMSE': 2.4040294, 'Time taken': 0.012180805206298828}
153.7s 1018 {'Model': 'KernelRidge', 'R-Squared': -0.5667537075482836, 'Adjusted R-Squared': -7.61714539151556, 'RMSE': 11.917691, 'Time taken': 0.011812448501586914}
153.7s 1019 {'Model': 'Lars', 'R-Squared': 0.9921355143250994, 'Adjusted R-Squared': 0.9567453287880466, 'RMSE': 0.8443586, 'Time taken': 0.011857986450195312}
153.7s 1020 {'Model': 'LarsCV', 'R-Squared': 0.9924445259832135, 'Adjusted R-Squared': 0.9584448929076744, 'RMSE': 0.8276041, 'Time taken': 0.02479267120361328}
153.7s 1021 {'Model': 'Lasso', 'R-Squared': 0.9501968145776902, 'Adjusted R-Squared': 0.7260824801772963, 'RMSE': 2.1248112, 'Time taken': 0.010523557662963867}
153.7s 1022 {'Model': 'LassoCV', 'R-Squared': 0.9811567322013247, 'Adjusted R-Squared': 0.8963620271072859, 'RMSE': 1.3069829, 'Time taken': 0.06326603889465332}
153.7s 1023 {'Model': 'LassoLars', 'R-Squared': 0.039816535458089164, 'Adjusted R-Squared': -4.28100905498051, 'RMSE': 9.329726, 'Time taken': 0.011531591415405273}
153.7s 1024 {'Model': 'LassoLarsCV', 'R-Squared': 0.9921408665234792, 'Adjusted R-Squared': 0.9567747658791357, 'RMSE': 0.8440712, 'Time taken': 0.03139853477478027}
153.7s 1025 {'Model': 'LassoLarsIC', 'R-Squared': 0.9927272123211116, 'Adjusted R-Squared': 0.9599996677661138, 'RMSE': 0.81197417, 'Time taken': 0.014095067977905273}
153.7s 1026 {'Model': 'LinearRegression', 'R-Squared': 0.9921361746426414, 'Adjusted R-Squared': 0.9567489605345275, 'RMSE': 0.84432316, 'Time taken': 0.009742498397827148}
153.9s 1027 {'Model': 'LinearSVR', 'R-Squared': 0.9371046195057666, 'Adjusted R-Squared': 0.6540754072817164, 'RMSE': 2.387817667806175, 'Time taken': 0.011287450790405273}
153.9s 1028 {'Model': 'MLPRegressor', 'R-Squared': 0.5668621051312204, 'Adjusted R-Squared': -1.382258421778288, 'RMSE': 6.2662096, 'Time taken': 0.12961626052856445}
153.9s 1029 {'Model': 'NuSVR', 'R-Squared': 0.6966660884417997, 'Adjusted R-Squared': -0.6683365135701018, 'RMSE': 5.243874262260156, 'Time taken': 0.01142740249633789}
153.9s 1030 {'Model': 'OrthogonalMatchingPursuit', 'R-Squared': 0.9745627204905936, 'Adjusted R-Squared': 0.8600949626982646, 'RMSE': 1.5185430830962725, 'Time taken': 0.010805130004882812}
153.9s 1031 {'Model': 'OrthogonalMatchingPursuitCV', 'R-Squared': 0.9835016711683352, 'Adjusted R-Squared': 0.9092591914258437, 'RMSE': 1.2229586258099088, 'Time taken': 0.01684737205505371}
153.9s 1032 {'Model': 'PassiveAggressiveRegressor', 'R-Squared': 0.9595059526282823, 'Adjusted R-Squared': 0.7772827394555527, 'RMSE': 1.915964156756527, 'Time taken': 0.009833097457885742}
153.9s 1033 {'Model': 'PoissonRegressor', 'R-Squared': 0.9635986894997732, 'Adjusted R-Squared': 0.7997927922487528, 'RMSE': 1.816562298520748, 'Time taken': 0.014385223388671875}
154.2s 1034 {'Model': 'QuantileRegressor', 'R-Squared': -0.4921086707759941, 'Adjusted R-Squared': -7.2065976892679675, 'RMSE': 11.630329365944784, 'Time taken': 0.09786224365234375}
154.2s 1035 {'Model': 'RANSACRegressor', 'R-Squared': 0.9909604413445485, 'Adjusted R-Squared': 0.9502824273950169, 'RMSE': 0.90524346, 'Time taken': 0.03687763214111328}
154.5s 1036 {'Model': 'RandomForestRegressor', 'R-Squared': 0.976882028852792, 'Adjusted R-Squared': 0.8728511586903558, 'RMSE': 1.4476602363557243, 'Time taken': 0.17976713180541992}
154.5s 1037 {'Model': 'Ridge', 'R-Squared': 0.96264684450401, 'Adjusted R-Squared': 0.7945576447720547, 'RMSE': 1.8401593, 'Time taken': 0.009980916976928711}
154.5s 1038 {'Model': 'RidgeCV', 'R-Squared': 0.9804559480569417, 'Adjusted R-Squared': 0.8925077143131793, 'RMSE': 1.3310644699636949, 'Time taken': 0.009815692901611328}
154.5s 1039 {'Model': 'SGDRegressor', 'R-Squared': 0.9552262765623147, 'Adjusted R-Squared': 0.753744521092731, 'RMSE': 2.0146675578600366, 'Time taken': 0.011747598648071289}
154.5s 1040 {'Model': 'SVR', 'R-Squared': 0.715907285250415, 'Adjusted R-Squared': -0.5625099311227173, 'RMSE': 5.074833935189616, 'Time taken': 0.009526491165161133}
154.5s 1041 {'Model': 'TransformedTargetRegressor', 'R-Squared': 0.9921361746426414, 'Adjusted R-Squared': 0.9567489605345275, 'RMSE': 0.84432316, 'Time taken': 0.009740591049194336}
154.5s 1042 {'Model': 'TweedieRegressor', 'R-Squared': 0.783575288263807, 'Adjusted R-Squared': -0.19033591454906174, 'RMSE': 4.429403155979621, 'Time taken': 0.010534524917602539}
154.8s 1043 {'Model': 'XGBRegressor', 'R-Squared': 0.9736684479778783, 'Adjusted R-Squared': 0.8551764638783308, 'RMSE': 1.5450054, 'Time taken': 0.37429141998291016}
154.8s 1044 {'Model': 'LGBMRegressor', 'R-Squared': 0.6804430209303982, 'Adjusted R-Squared': -0.7575633848828098, 'RMSE': 5.382275702185803, 'Time taken': 0.028052091598510742}
154.8s 1045 Project: indian-economy-from-1960-to-2020
154.8s 1046 indian-economy-from-1960-to-2020
154.8s 1047 Target: Imports of goods and services (% of GDP)
154.8s 1048 Imports of goods and services (% of GDP)
154.8s 1049 Target Standard Deviation: 7.58313512802124
154.8s 1050 Adjusted R-Squared  R-Squared  RMSE  Time Taken
154.8s 1051 Model
154.8s 1052 LassoLarsIC                                  0.96       0.99  0.81        0.01
154.8s 1053 LarsCV                                       0.96       0.99  0.83        0.02
154.8s 1054 HuberRegressor                               0.96       0.99  0.83        0.04
154.8s 1055 LassoLarsCV                                  0.96       0.99  0.84        0.03
154.8s 1056 TransformedTargetRegressor                   0.96       0.99  0.84        0.01
154.8s 1057 LinearRegression                             0.96       0.99  0.84        0.01
154.8s 1058 Lars                                         0.96       0.99  0.84        0.01
154.8s 1059 RANSACRegressor                              0.95       0.99  0.91        0.04
154.8s 1060 ExtraTreesRegressor                          0.91       0.98  1.19        0.11
154.8s 1061 BaggingRegressor                             0.91       0.98  1.22        0.03
154.8s 1062 OrthogonalMatchingPursuitCV                  0.91       0.98  1.22        0.02
154.8s 1063 BayesianRidge                                0.90       0.98  1.26        0.01
154.8s 1064 LassoCV                                      0.90       0.98  1.31        0.06
154.8s 1065 RidgeCV                                      0.89       0.98  1.33        0.01
154.8s 1066 RandomForestRegressor                        0.87       0.98  1.45        0.18
154.8s 1067 OrthogonalMatchingPursuit                    0.86       0.97  1.52        0.01
154.8s 1068 XGBRegressor                                 0.86       0.97  1.55        0.37
154.8s 1069 ElasticNetCV                                 0.85       0.97  1.55        0.06
154.8s 1070 ExtraTreeRegressor                           0.84       0.97  1.61        0.01
154.8s 1071 AdaBoostRegressor                            0.80       0.96  1.81        0.08
154.8s 1072 PoissonRegressor                             0.80       0.96  1.82        0.01
154.8s 1073 Ridge                                        0.79       0.96  1.84        0.01
154.8s 1074 GradientBoostingRegressor                    0.78       0.96  1.91        0.09
154.8s 1075 PassiveAggressiveRegressor                   0.78       0.96  1.92        0.01
154.8s 1076 SGDRegressor                                 0.75       0.96  2.01        0.01
154.8s 1077 Lasso                                        0.73       0.95  2.12        0.01
154.8s 1078 LinearSVR                                    0.65       0.94  2.39        0.01
154.8s 1079 KNeighborsRegressor                          0.65       0.94  2.40        0.01
154.8s 1080 DecisionTreeRegressor                        0.13       0.84  3.79        0.01
154.8s 1081 ElasticNet                                  -0.09       0.80  4.23        0.01
154.8s 1082 TweedieRegressor                            -0.19       0.78  4.43        0.01
154.8s 1083 GammaRegressor                              -0.28       0.77  4.60        0.01
154.8s 1084 SVR                                         -0.56       0.72  5.07        0.01
154.8s 1085 NuSVR                                       -0.67       0.70  5.24        0.01
154.8s 1086 LGBMRegressor                               -0.76       0.68  5.38        0.03
154.8s 1087 HistGradientBoostingRegressor               -0.88       0.66  5.57        0.06
154.8s 1088 MLPRegressor                                -1.38       0.57  6.27        0.13
154.8s 1089 GaussianProcessRegressor                    -2.39       0.38  7.48        0.01
154.8s 1090 LassoLars                                   -4.28       0.04  9.33        0.01
154.8s 1091 DummyRegressor                              -5.03      -0.10  9.97        0.01
154.8s 1092 QuantileRegressor                           -7.21      -0.49 11.63        0.10
154.8s 1093 KernelRidge                                 -7.62      -0.57 11.92        0.01
154.8s 1094 LEARNING RATE: 0.1
154.8s 1095 0%|          | 0/42 [00:00<?, ?it/s]  5%|▍         | 2/42 [00:00<00:02, 18.62it/s] 17%|█▋        | 7/42 [00:00<00:00, 35.84it/s] 26%|██▌       | 11/42 [00:00<00:01, 30.47it/s] 36%|███▌      | 15/42 [00:00<00:01, 24.73it/s] 48%|████▊     | 20/42 [00:00<00:00, 29.52it/s] 62%|██████▏   | 26/42 [00:00<00:00, 29.16it/s] 76%|███████▌  | 32/42 [00:01<00:00, 31.62it/s] 86%|████████▌ | 36/42 [00:01<00:00, 25.64it/s] 98%|█████████▊| 41/42 [00:01<00:00, 18.74it/s]100%|██████████| 42/42 [00:01<00:00, 23.92it/s]
154.8s 1096 Better model found at epoch 0 with _rmse value: 31.274829864501953.
154.9s 1097 No improvement since epoch 0: early stopping
155.4s 1098 XGBoost Predictions vs Actual==========
155.4s 1099 actual  predicted
155.4s 1100 0   11.93      12.75
155.4s 1101 1    9.82      10.30
155.4s 1102 2   29.27      30.51
155.4s 1103 3   28.41      31.26
155.4s 1104 4    8.49       9.41
155.4s 1105 XGBoost RMSE:  1.5450054
155.8s 1106 Target Variable: GDP growth (annual %)
155.8s 1107 CATS=====================
155.8s 1108 []
155.8s 1109 CONTS=====================
155.8s 1110 ['GDP (current US$) ', ' GDP per capita (current US$) ', 'Imports of goods and services (% of GDP)', 'Exports of goods and services (% of GDP)', ' Total reserves (includes gold, current US$) ', 'Inflation, consumer prices (annual %)', 'Population, total', 'Population growth (annual %)', 'Life expectancy at birth, total (years)']
155.8s 1111 9
155.8s 1112 Looping through continuous variables to find breakpoint
155.8s 1113 Continuous variables that made the cut : ['GDP (current US$) ', ' GDP per capita (current US$) ', 'Imports of goods and services (% of GDP)', 'Exports of goods and services (% of GDP)', ' Total reserves (includes gold, current US$) ', 'Inflation, consumer prices (annual %)', 'Population, total', 'Population growth (annual %)', 'Life expectancy at birth, total (years)']
155.8s 1114 Categorical variables that made the cut : []
155.8s 1115 Tabular Object size: 61
155.8s 1116 problem with getting one batch of indian-economy-from-1960-to-2020
156.0s 1117 {'Model': 'AdaBoostRegressor', 'R-Squared': -0.5897288181416143, 'Adjusted R-Squared': -7.743508499778878, 'RMSE': 3.155226047104894, 'Time taken': 0.07925772666931152}
156.0s 1118 {'Model': 'BaggingRegressor', 'R-Squared': -0.622815970903658, 'Adjusted R-Squared': -7.925487839970119, 'RMSE': 3.1878919387263607, 'Time taken': 0.03028249740600586}
156.0s 1119 {'Model': 'BayesianRidge', 'R-Squared': -0.06391754090243595, 'Adjusted R-Squared': -4.851546474963397, 'RMSE': 2.581207626063647, 'Time taken': 0.015270471572875977}
156.0s 1120 {'Model': 'DecisionTreeRegressor', 'R-Squared': -2.934217908513047, 'Adjusted R-Squared': -20.638198496821758, 'RMSE': 4.963615823962575, 'Time taken': 0.010511636734008789}
156.0s 1121 {'Model': 'DummyRegressor', 'R-Squared': -0.02976430424793386, 'Adjusted R-Squared': -4.663703673363636, 'RMSE': 2.5394397, 'Time taken': 0.009638547897338867}
156.0s 1122 {'Model': 'ElasticNet', 'R-Squared': 0.03661924570517672, 'Adjusted R-Squared': -4.298594148621528, 'RMSE': 2.4562237, 'Time taken': 0.01047968864440918}
156.1s 1123 {'Model': 'ElasticNetCV', 'R-Squared': 0.023003679730022042, 'Adjusted R-Squared': -4.373479761484878, 'RMSE': 2.47352, 'Time taken': 0.11129951477050781}
156.1s 1124 {'Model': 'ExtraTreeRegressor', 'R-Squared': -0.7497892991658848, 'Adjusted R-Squared': -8.623841145412367, 'RMSE': 3.3102579182093805, 'Time taken': 0.011391162872314453}
156.2s 1125 {'Model': 'ExtraTreesRegressor', 'R-Squared': -0.2186714203430007, 'Adjusted R-Squared': -5.702692811886504, 'RMSE': 2.762563491629579, 'Time taken': 0.11363816261291504}
156.2s 1126 GammaRegressor model failed to execute
156.2s 1127 Some value(s) of y are out of the valid range for family GammaDistribution
156.2s 1128 {'Model': 'GaussianProcessRegressor', 'R-Squared': -6.376303135051569, 'Adjusted R-Squared': -39.56966724278363, 'RMSE': 6.796547132612042, 'Time taken': 0.019116640090942383}
156.4s 1129 {'Model': 'GradientBoostingRegressor', 'R-Squared': -0.44134064744308166, 'Adjusted R-Squared': -6.92737356093695, 'RMSE': 3.0043620821509993, 'Time taken': 0.09641528129577637}
156.4s 1130 {'Model': 'HistGradientBoostingRegressor', 'R-Squared': 0.0677274156757679, 'Adjusted R-Squared': -4.127499213783277, 'RMSE': 2.4162419015006926, 'Time taken': 0.0567476749420166}
156.5s 1131 {'Model': 'HuberRegressor', 'R-Squared': -0.2955448142387789, 'Adjusted R-Squared': -6.125496478313284, 'RMSE': 2.848361946653708, 'Time taken': 0.038423776626586914}
156.5s 1132 {'Model': 'KNeighborsRegressor', 'R-Squared': -0.26502004265073764, 'Adjusted R-Squared': -5.957610234579057, 'RMSE': 2.8146064, 'Time taken': 0.011069536209106445}
156.5s 1133 {'Model': 'KernelRidge', 'R-Squared': -4.814571225398215, 'Adjusted R-Squared': -30.980141739690183, 'RMSE': 6.0343127, 'Time taken': 0.010133028030395508}
156.5s 1134 {'Model': 'Lars', 'R-Squared': -2.828278286053293, 'Adjusted R-Squared': -20.05553057329311, 'RMSE': 4.89633, 'Time taken': 0.011448860168457031}
156.5s 1135 {'Model': 'LarsCV', 'R-Squared': 0.011327874760415635, 'Adjusted R-Squared': -4.437696688817714, 'RMSE': 2.4882565, 'Time taken': 0.023650407791137695}
156.5s 1136 {'Model': 'Lasso', 'R-Squared': -0.02976430424793386, 'Adjusted R-Squared': -4.663703673363636, 'RMSE': 2.5394397, 'Time taken': 0.010144472122192383}
156.8s 1137 {'Model': 'LassoCV', 'R-Squared': -0.24289225263723568, 'Adjusted R-Squared': -5.835907389504796, 'RMSE': 2.789881, 'Time taken': 0.1533045768737793}
156.8s 1138 {'Model': 'LassoLars', 'R-Squared': -0.02976430424793386, 'Adjusted R-Squared': -4.663703673363636, 'RMSE': 2.5394397, 'Time taken': 0.010780096054077148}
156.8s 1139 {'Model': 'LassoLarsCV', 'R-Squared': -0.33675198690492714, 'Adjusted R-Squared': -6.352135927977099, 'RMSE': 2.8933063, 'Time taken': 0.03330111503601074}
156.8s 1140 {'Model': 'LassoLarsIC', 'R-Squared': -0.28164520191642617, 'Adjusted R-Squared': -6.049048610540344, 'RMSE': 2.833041, 'Time taken': 0.015398740768432617}
156.8s 1141 {'Model': 'LinearRegression', 'R-Squared': -0.33661189985635764, 'Adjusted R-Squared': -6.351365449209967, 'RMSE': 2.8931546, 'Time taken': 0.010463953018188477}
156.8s 1142 {'Model': 'LinearSVR', 'R-Squared': -0.41919453431278764, 'Adjusted R-Squared': -6.805569938720332, 'RMSE': 2.981191813016879, 'Time taken': 0.011366605758666992}
156.8s 1143 {'Model': 'MLPRegressor', 'R-Squared': -0.9341155707590452, 'Adjusted R-Squared': -9.637635639174748, 'RMSE': 3.4802477, 'Time taken': 0.12323713302612305}
157.0s 1144 {'Model': 'NuSVR', 'R-Squared': 0.11687632351051447, 'Adjusted R-Squared': -3.857180220692171, 'RMSE': 2.3516880867199577, 'Time taken': 0.011661767959594727}
157.0s 1145 {'Model': 'OrthogonalMatchingPursuit', 'R-Squared': 0.10649792941443648, 'Adjusted R-Squared': -3.9142613882205994, 'RMSE': 2.3654661441876037, 'Time taken': 0.010255098342895508}
157.0s 1146 {'Model': 'OrthogonalMatchingPursuitCV', 'R-Squared': -0.00011770701003399608, 'Adjusted R-Squared': -4.500647388555187, 'RMSE': 2.5026177078350402, 'Time taken': 0.015755414962768555}
157.0s 1147 {'Model': 'PassiveAggressiveRegressor', 'R-Squared': -0.6614249231508624, 'Adjusted R-Squared': -8.137837077329744, 'RMSE': 3.2255911247900824, 'Time taken': 0.009667396545410156}
157.0s 1148 PoissonRegressor model failed to execute
157.0s 1149 Some value(s) of y are out of the valid range for family PoissonDistribution
157.0s 1150 {'Model': 'QuantileRegressor', 'R-Squared': -0.009585039769663739, 'Adjusted R-Squared': -4.552717718733151, 'RMSE': 2.514434970555741, 'Time taken': 0.07485795021057129}
157.3s 1151 {'Model': 'RANSACRegressor', 'R-Squared': -0.7296240352617225, 'Adjusted R-Squared': -8.512932193939474, 'RMSE': 3.2911282, 'Time taken': 0.12327241897583008}
157.3s 1152 {'Model': 'RandomForestRegressor', 'R-Squared': -0.2863490266745641, 'Adjusted R-Squared': -6.074919646710103, 'RMSE': 2.8382350964746434, 'Time taken': 0.14484882354736328}
157.3s 1153 {'Model': 'Ridge', 'R-Squared': -0.1268463836977749, 'Adjusted R-Squared': -5.197655110337762, 'RMSE': 2.656448, 'Time taken': 0.010199308395385742}
157.3s 1154 {'Model': 'RidgeCV', 'R-Squared': -0.07241151242496535, 'Adjusted R-Squared': -4.898263318337309, 'RMSE': 2.5914909032528484, 'Time taken': 0.010159015655517578}
157.3s 1155 {'Model': 'SGDRegressor', 'R-Squared': -0.07672781314508259, 'Adjusted R-Squared': -4.922002972297954, 'RMSE': 2.5967008536110785, 'Time taken': 0.011772871017456055}
157.3s 1156 {'Model': 'SVR', 'R-Squared': 0.12136084259525581, 'Adjusted R-Squared': -3.832515365726093, 'RMSE': 2.3457095284906404, 'Time taken': 0.009591102600097656}
157.3s 1157 {'Model': 'TransformedTargetRegressor', 'R-Squared': -0.33661189985635764, 'Adjusted R-Squared': -6.351365449209967, 'RMSE': 2.8931546, 'Time taken': 0.009810686111450195}
157.5s 1158 {'Model': 'TweedieRegressor', 'R-Squared': -0.05292950129308749, 'Adjusted R-Squared': -4.7911122571119815, 'RMSE': 2.567843797459513, 'Time taken': 0.013823270797729492}
157.7s 1159 {'Model': 'XGBRegressor', 'R-Squared': -0.6016891683880254, 'Adjusted R-Squared': -7.80929042613414, 'RMSE': 3.1670732, 'Time taken': 0.37694478034973145}
157.7s 1160 {'Model': 'LGBMRegressor', 'R-Squared': 0.09070482164056748, 'Adjusted R-Squared': -4.0011234809768785, 'RMSE': 2.3862799874164984, 'Time taken': 0.030744314193725586}
157.7s 1161 Project: indian-economy-from-1960-to-2020
157.7s 1162 indian-economy-from-1960-to-2020
157.7s 1163 Target: GDP growth (annual %)
157.7s 1164 GDP growth (annual %)
157.7s 1165 Target Standard Deviation: 3.482764482498169
157.7s 1166 Adjusted R-Squared  R-Squared  RMSE  Time Taken
157.7s 1167 Model
157.7s 1168 SVR                                         -3.83       0.12  2.35        0.01
157.7s 1169 NuSVR                                       -3.86       0.12  2.35        0.01
157.7s 1170 OrthogonalMatchingPursuit                   -3.91       0.11  2.37        0.01
157.7s 1171 LGBMRegressor                               -4.00       0.09  2.39        0.03
157.7s 1172 HistGradientBoostingRegressor               -4.13       0.07  2.42        0.06
157.7s 1173 ElasticNet                                  -4.30       0.04  2.46        0.01
157.7s 1174 ElasticNetCV                                -4.37       0.02  2.47        0.11
157.7s 1175 LarsCV                                      -4.44       0.01  2.49        0.02
157.7s 1176 OrthogonalMatchingPursuitCV                 -4.50      -0.00  2.50        0.02
157.7s 1177 QuantileRegressor                           -4.55      -0.01  2.51        0.07
157.7s 1178 DummyRegressor                              -4.66      -0.03  2.54        0.01
157.7s 1179 Lasso                                       -4.66      -0.03  2.54        0.01
157.7s 1180 LassoLars                                   -4.66      -0.03  2.54        0.01
157.7s 1181 TweedieRegressor                            -4.79      -0.05  2.57        0.01
157.7s 1182 BayesianRidge                               -4.85      -0.06  2.58        0.02
157.7s 1183 RidgeCV                                     -4.90      -0.07  2.59        0.01
157.7s 1184 SGDRegressor                                -4.92      -0.08  2.60        0.01
157.7s 1185 Ridge                                       -5.20      -0.13  2.66        0.01
157.7s 1186 ExtraTreesRegressor                         -5.70      -0.22  2.76        0.11
157.7s 1187 LassoCV                                     -5.84      -0.24  2.79        0.15
157.7s 1188 KNeighborsRegressor                         -5.96      -0.27  2.81        0.01
157.7s 1189 LassoLarsIC                                 -6.05      -0.28  2.83        0.02
157.7s 1190 RandomForestRegressor                       -6.07      -0.29  2.84        0.14
157.7s 1191 HuberRegressor                              -6.13      -0.30  2.85        0.04
157.7s 1192 LinearRegression                            -6.35      -0.34  2.89        0.01
157.7s 1193 TransformedTargetRegressor                  -6.35      -0.34  2.89        0.01
157.7s 1194 LassoLarsCV                                 -6.35      -0.34  2.89        0.03
157.7s 1195 LinearSVR                                   -6.81      -0.42  2.98        0.01
157.7s 1196 GradientBoostingRegressor                   -6.93      -0.44  3.00        0.10
157.7s 1197 AdaBoostRegressor                           -7.74      -0.59  3.16        0.08
157.7s 1198 XGBRegressor                                -7.81      -0.60  3.17        0.38
157.7s 1199 BaggingRegressor                            -7.93      -0.62  3.19        0.03
157.7s 1200 PassiveAggressiveRegressor                  -8.14      -0.66  3.23        0.01
157.7s 1201 RANSACRegressor                             -8.51      -0.73  3.29        0.12
157.7s 1202 ExtraTreeRegressor                          -8.62      -0.75  3.31        0.01
157.7s 1203 MLPRegressor                                -9.64      -0.93  3.48        0.12
157.7s 1204 Lars                                       -20.06      -2.83  4.90        0.01
157.7s 1205 DecisionTreeRegressor                      -20.64      -2.93  4.96        0.01
157.7s 1206 KernelRidge                                -30.98      -4.81  6.03        0.01
157.7s 1207 GaussianProcessRegressor                   -39.57      -6.38  6.80        0.02
157.7s 1208 LEARNING RATE: 0.1
157.7s 1209 0%|          | 0/42 [00:00<?, ?it/s]  5%|▍         | 2/42 [00:00<00:02, 18.23it/s] 17%|█▋        | 7/42 [00:00<00:01, 27.18it/s] 24%|██▍       | 10/42 [00:00<00:01, 25.07it/s] 31%|███       | 13/42 [00:00<00:01, 21.50it/s] 45%|████▌     | 19/42 [00:00<00:00, 31.21it/s] 55%|█████▍    | 23/42 [00:00<00:00, 25.59it/s] 62%|██████▏   | 26/42 [00:01<00:00, 24.04it/s] 76%|███████▌  | 32/42 [00:01<00:00, 30.22it/s] 86%|████████▌ | 36/42 [00:01<00:00, 22.45it/s] 98%|█████████▊| 41/42 [00:01<00:00, 17.18it/s]100%|██████████| 42/42 [00:01<00:00, 21.84it/s]
157.8s 1210 Better model found at epoch 0 with _rmse value: 7.4152936935424805.
157.8s 1211 No improvement since epoch 0: early stopping
158.3s 1212 XGBoost Predictions vs Actual==========
158.3s 1213 actual  predicted
158.3s 1214 0    9.15       2.02
158.3s 1215 1    1.64       4.25
158.3s 1216 2    3.82       5.42
158.3s 1217 3    7.55       7.87
158.3s 1218 4    4.05       7.83
158.3s 1219 XGBoost RMSE:  3.1670732
158.7s 1220 Target Variable:  GDP per capita (current US$)
158.7s 1221 CATS=====================
158.7s 1222 []
158.7s 1223 CONTS=====================
158.7s 1224 ['GDP (current US$) ', 'GDP growth (annual %)', 'Imports of goods and services (% of GDP)', 'Exports of goods and services (% of GDP)', ' Total reserves (includes gold, current US$) ', 'Inflation, consumer prices (annual %)', 'Population, total', 'Population growth (annual %)', 'Life expectancy at birth, total (years)']
158.7s 1225 9
158.7s 1226 Looping through continuous variables to find breakpoint
158.7s 1227 Continuous variables that made the cut : ['GDP (current US$) ', 'GDP growth (annual %)', 'Imports of goods and services (% of GDP)', 'Exports of goods and services (% of GDP)', ' Total reserves (includes gold, current US$) ', 'Inflation, consumer prices (annual %)', 'Population, total', 'Population growth (annual %)', 'Life expectancy at birth, total (years)']
158.7s 1228 Categorical variables that made the cut : []
158.7s 1229 Tabular Object size: 61
158.7s 1230 problem with getting one batch of indian-economy-from-1960-to-2020
159.0s 1231 {'Model': 'AdaBoostRegressor', 'R-Squared': 0.9692460416328266, 'Adjusted R-Squared': 0.8308532289805461, 'RMSE': 41.93469775733455, 'Time taken': 0.0769813060760498}
159.0s 1232 {'Model': 'BaggingRegressor', 'R-Squared': 0.950470773072707, 'Adjusted R-Squared': 0.7275892518998885, 'RMSE': 53.21741569574132, 'Time taken': 0.027173519134521484}
159.0s 1233 {'Model': 'BayesianRidge', 'R-Squared': 0.9979564903095223, 'Adjusted R-Squared': 0.9887606967023725, 'RMSE': 10.809643143227937, 'Time taken': 0.012189388275146484}
159.0s 1234 {'Model': 'DecisionTreeRegressor', 'R-Squared': 0.9682874158473503, 'Adjusted R-Squared': 0.8255807871604268, 'RMSE': 42.58325179379016, 'Time taken': 0.010410308837890625}
159.0s 1235 {'Model': 'DummyRegressor', 'R-Squared': -0.7799768266531317, 'Adjusted R-Squared': -8.789872546592225, 'RMSE': 319.02902, 'Time taken': 0.009250879287719727}
159.0s 1236 {'Model': 'ElasticNet', 'R-Squared': 0.7109837964019355, 'Adjusted R-Squared': -0.5895891197893546, 'RMSE': 128.55356, 'Time taken': 0.010410547256469727}
159.0s 1237 {'Model': 'ElasticNetCV', 'R-Squared': 0.6881164500636548, 'Adjusted R-Squared': -0.7153595246498983, 'RMSE': 133.54242, 'Time taken': 0.06298065185546875}
159.0s 1238 {'Model': 'ExtraTreeRegressor', 'R-Squared': 0.9576849779010945, 'Adjusted R-Squared': 0.7672673784560199, 'RMSE': 49.189260345458884, 'Time taken': 0.011075019836425781}
159.2s 1239 {'Model': 'ExtraTreesRegressor', 'R-Squared': 0.9855058772343928, 'Adjusted R-Squared': 0.9202823247891602, 'RMSE': 28.788495821537232, 'Time taken': 0.11443710327148438}
159.2s 1240 {'Model': 'GammaRegressor', 'R-Squared': 0.9506524007667032, 'Adjusted R-Squared': 0.7285882042168677, 'RMSE': 53.119749785564224, 'Time taken': 0.012600183486938477}
159.2s 1241 {'Model': 'GaussianProcessRegressor', 'R-Squared': 0.9183786945459609, 'Adjusted R-Squared': 0.5510828200027849, 'RMSE': 68.31636881433602, 'Time taken': 0.012936592102050781}
159.2s 1242 {'Model': 'GradientBoostingRegressor', 'R-Squared': 0.9768217066948832, 'Adjusted R-Squared': 0.8725193868218577, 'RMSE': 36.4052261531002, 'Time taken': 0.08705520629882812}
159.2s 1243 {'Model': 'HistGradientBoostingRegressor', 'R-Squared': -2.866864919821231, 'Adjusted R-Squared': -20.26775705901677, 'RMSE': 470.22152622904, 'Time taken': 0.056543827056884766}
159.5s 1244 {'Model': 'HuberRegressor', 'R-Squared': 0.9979296612129192, 'Adjusted R-Squared': 0.9886131366710553, 'RMSE': 10.880371280541828, 'Time taken': 0.03783464431762695}
159.5s 1245 {'Model': 'KNeighborsRegressor', 'R-Squared': 0.8403220509401663, 'Adjusted R-Squared': 0.12177128017091476, 'RMSE': 95.55325, 'Time taken': 0.011077642440795898}
159.5s 1246 {'Model': 'KernelRidge', 'R-Squared': -5.542735764469906, 'Adjusted R-Squared': -34.985046704584484, 'RMSE': 611.64966, 'Time taken': 0.011092185974121094}
159.5s 1247 {'Model': 'Lars', 'R-Squared': -0.20557907905910278, 'Adjusted R-Squared': -5.630684934825065, 'RMSE': 262.55533, 'Time taken': 0.01237630844116211}
159.5s 1248 {'Model': 'LarsCV', 'R-Squared': 0.9912244806480789, 'Adjusted R-Squared': 0.9517346435644338, 'RMSE': 22.400589, 'Time taken': 0.022932767868041992}
159.5s 1249 {'Model': 'Lasso', 'R-Squared': 0.9936353941872371, 'Adjusted R-Squared': 0.9649946680298042, 'RMSE': 19.076942, 'Time taken': 0.01029205322265625}
159.5s 1250 {'Model': 'LassoCV', 'R-Squared': 0.9953967881357207, 'Adjusted R-Squared': 0.9746823347464642, 'RMSE': 16.223835, 'Time taken': 0.05713081359863281}
159.5s 1251 {'Model': 'LassoLars', 'R-Squared': 0.9909125903048933, 'Adjusted R-Squared': 0.9500192466769133, 'RMSE': 22.795181, 'Time taken': 0.012419462203979492}
159.5s 1252 {'Model': 'LassoLarsCV', 'R-Squared': 0.9973270260639966, 'Adjusted R-Squared': 0.9852986433519813, 'RMSE': 12.362901, 'Time taken': 0.02602362632751465}
159.5s 1253 {'Model': 'LassoLarsIC', 'R-Squared': 0.997954964868091, 'Adjusted R-Squared': 0.9887523067745004, 'RMSE': 10.813677, 'Time taken': 0.012967109680175781}
159.5s 1254 {'Model': 'LinearRegression', 'R-Squared': 0.997971228861934, 'Adjusted R-Squared': 0.9888417587406371, 'RMSE': 10.770591, 'Time taken': 0.009444236755371094}
159.5s 1255 {'Model': 'LinearSVR', 'R-Squared': -2.2278586793288766, 'Adjusted R-Squared': -16.75322273630882, 'RMSE': 429.6158171005424, 'Time taken': 0.009279727935791016}
159.8s 1256 {'Model': 'MLPRegressor', 'R-Squared': -2.629045738304234, 'Adjusted R-Squared': -18.959751560673286, 'RMSE': 455.53235, 'Time taken': 0.12616443634033203}
159.8s 1257 {'Model': 'NuSVR', 'R-Squared': -0.5538745911796759, 'Adjusted R-Squared': -7.546310251488217, 'RMSE': 298.0787310696789, 'Time taken': 0.010269880294799805}
159.8s 1258 {'Model': 'OrthogonalMatchingPursuit', 'R-Squared': 0.9840461518638834, 'Adjusted R-Squared': 0.912253835251359, 'RMSE': 30.20339295629949, 'Time taken': 0.009469985961914062}
159.8s 1259 {'Model': 'OrthogonalMatchingPursuitCV', 'R-Squared': 0.9928849041426637, 'Adjusted R-Squared': 0.9608669727846505, 'RMSE': 20.170347660554754, 'Time taken': 0.015018463134765625}
159.8s 1260 {'Model': 'PassiveAggressiveRegressor', 'R-Squared': 0.9897438835283248, 'Adjusted R-Squared': 0.9435913594057862, 'RMSE': 24.216673041810616, 'Time taken': 0.00973057746887207}
159.8s 1261 {'Model': 'PoissonRegressor', 'R-Squared': 0.98722040116195, 'Adjusted R-Squared': 0.9297122063907248, 'RMSE': 27.032213992342047, 'Time taken': 0.024245500564575195}
159.8s 1262 {'Model': 'QuantileRegressor', 'R-Squared': -0.18523597942131165, 'Adjusted R-Squared': -5.5187978868172145, 'RMSE': 260.3307199644342, 'Time taken': 0.10270261764526367}
160.0s 1263 {'Model': 'RANSACRegressor', 'R-Squared': 0.9979712457384756, 'Adjusted R-Squared': 0.988841851561616, 'RMSE': 10.770546, 'Time taken': 0.02918553352355957}
160.0s 1264 {'Model': 'RandomForestRegressor', 'R-Squared': 0.9580275877770424, 'Adjusted R-Squared': 0.7691517327737334, 'RMSE': 48.9897215410199, 'Time taken': 0.1843395233154297}
160.0s 1265 {'Model': 'Ridge', 'R-Squared': 0.9797212886448733, 'Adjusted R-Squared': 0.888467087546803, 'RMSE': 34.052044, 'Time taken': 0.010040521621704102}
160.2s 1266 {'Model': 'RidgeCV', 'R-Squared': 0.9969898926212521, 'Adjusted R-Squared': 0.9834444094168868, 'RMSE': 13.119400808482775, 'Time taken': 0.012155294418334961}
160.2s 1267 {'Model': 'SGDRegressor', 'R-Squared': 0.9916246138278844, 'Adjusted R-Squared': 0.953935376053364, 'RMSE': 21.883935518855615, 'Time taken': 0.017812490463256836}
160.2s 1268 {'Model': 'SVR', 'R-Squared': -0.11992470510019149, 'Adjusted R-Squared': -5.159585878051053, 'RMSE': 253.05645434633806, 'Time taken': 0.010015010833740234}
160.2s 1269 {'Model': 'TransformedTargetRegressor', 'R-Squared': 0.997971228861934, 'Adjusted R-Squared': 0.9888417587406371, 'RMSE': 10.770591, 'Time taken': 0.010114669799804688}
160.2s 1270 {'Model': 'TweedieRegressor', 'R-Squared': 0.6531286894498911, 'Adjusted R-Squared': -0.9077922080255989, 'RMSE': 140.8338969904872, 'Time taken': 0.011783599853515625}
160.5s 1271 {'Model': 'XGBRegressor', 'R-Squared': 0.9778493450435581, 'Adjusted R-Squared': 0.8781713977395698, 'RMSE': 35.589043, 'Time taken': 0.388751745223999}
160.5s 1272 {'Model': 'LGBMRegressor', 'R-Squared': -2.7106983688537865, 'Adjusted R-Squared': -19.408841028695825, 'RMSE': 460.6285293755474, 'Time taken': 0.030368328094482422}
160.5s 1273 Project: indian-economy-from-1960-to-2020
160.5s 1274 indian-economy-from-1960-to-2020
160.5s 1275 Target:  GDP per capita (current US$)
160.5s 1276 GDP per capita (current US$)
160.5s 1277 Target Standard Deviation: 628.4550170898438
160.5s 1278 Adjusted R-Squared  R-Squared   RMSE  \
160.5s 1279 Model
160.5s 1280 RANSACRegressor                              0.99       1.00  10.77
160.5s 1281 TransformedTargetRegressor                   0.99       1.00  10.77
160.5s 1282 LinearRegression                             0.99       1.00  10.77
160.5s 1283 BayesianRidge                                0.99       1.00  10.81
160.5s 1284 LassoLarsIC                                  0.99       1.00  10.81
160.5s 1285 HuberRegressor                               0.99       1.00  10.88
160.5s 1286 LassoLarsCV                                  0.99       1.00  12.36
160.5s 1287 RidgeCV                                      0.98       1.00  13.12
160.5s 1288 LassoCV                                      0.97       1.00  16.22
160.5s 1289 Lasso                                        0.96       0.99  19.08
160.5s 1290 OrthogonalMatchingPursuitCV                  0.96       0.99  20.17
160.5s 1291 SGDRegressor                                 0.95       0.99  21.88
160.5s 1292 LarsCV                                       0.95       0.99  22.40
160.5s 1293 LassoLars                                    0.95       0.99  22.80
160.5s 1294 PassiveAggressiveRegressor                   0.94       0.99  24.22
160.5s 1295 PoissonRegressor                             0.93       0.99  27.03
160.5s 1296 ExtraTreesRegressor                          0.92       0.99  28.79
160.5s 1297 OrthogonalMatchingPursuit                    0.91       0.98  30.20
160.5s 1298 Ridge                                        0.89       0.98  34.05
160.5s 1299 XGBRegressor                                 0.88       0.98  35.59
160.5s 1300 GradientBoostingRegressor                    0.87       0.98  36.41
160.5s 1301 AdaBoostRegressor                            0.83       0.97  41.93
160.5s 1302 DecisionTreeRegressor                        0.83       0.97  42.58
160.5s 1303 RandomForestRegressor                        0.77       0.96  48.99
160.5s 1304 ExtraTreeRegressor                           0.77       0.96  49.19
160.5s 1305 GammaRegressor                               0.73       0.95  53.12
160.5s 1306 BaggingRegressor                             0.73       0.95  53.22
160.5s 1307 GaussianProcessRegressor                     0.55       0.92  68.32
160.5s 1308 KNeighborsRegressor                          0.12       0.84  95.55
160.5s 1309 ElasticNet                                  -0.59       0.71 128.55
160.5s 1310 ElasticNetCV                                -0.72       0.69 133.54
160.5s 1311 TweedieRegressor                            -0.91       0.65 140.83
160.5s 1312 SVR                                         -5.16      -0.12 253.06
160.5s 1313 QuantileRegressor                           -5.52      -0.19 260.33
160.5s 1314 Lars                                        -5.63      -0.21 262.56
160.5s 1315 NuSVR                                       -7.55      -0.55 298.08
160.5s 1316 DummyRegressor                              -8.79      -0.78 319.03
160.5s 1317 LinearSVR                                  -16.75      -2.23 429.62
160.5s 1318 MLPRegressor                               -18.96      -2.63 455.53
160.5s 1319 LGBMRegressor                              -19.41      -2.71 460.63
160.5s 1320 HistGradientBoostingRegressor              -20.27      -2.87 470.22
160.5s 1321 KernelRidge                                -34.99      -5.54 611.65
160.5s 1322 
160.5s 1323 Time Taken
160.5s 1324 Model
160.5s 1325 RANSACRegressor                      0.03
160.5s 1326 TransformedTargetRegressor           0.01
160.5s 1327 LinearRegression                     0.01
160.5s 1328 BayesianRidge                        0.01
160.5s 1329 LassoLarsIC                          0.01
160.5s 1330 HuberRegressor                       0.04
160.5s 1331 LassoLarsCV                          0.03
160.5s 1332 RidgeCV                              0.01
160.5s 1333 LassoCV                              0.06
160.5s 1334 Lasso                                0.01
160.5s 1335 OrthogonalMatchingPursuitCV          0.02
160.5s 1336 SGDRegressor                         0.02
160.5s 1337 LarsCV                               0.02
160.5s 1338 LassoLars                            0.01
160.5s 1339 PassiveAggressiveRegressor           0.01
160.5s 1340 PoissonRegressor                     0.02
160.5s 1341 ExtraTreesRegressor                  0.11
160.5s 1342 OrthogonalMatchingPursuit            0.01
160.5s 1343 Ridge                                0.01
160.5s 1344 XGBRegressor                         0.39
160.5s 1345 GradientBoostingRegressor            0.09
160.5s 1346 AdaBoostRegressor                    0.08
160.5s 1347 DecisionTreeRegressor                0.01
160.5s 1348 RandomForestRegressor                0.18
160.5s 1349 ExtraTreeRegressor                   0.01
160.5s 1350 GammaRegressor                       0.01
160.5s 1351 BaggingRegressor                     0.03
160.5s 1352 GaussianProcessRegressor             0.01
160.5s 1353 KNeighborsRegressor                  0.01
160.5s 1354 ElasticNet                           0.01
160.5s 1355 ElasticNetCV                         0.06
160.5s 1356 TweedieRegressor                     0.01
160.5s 1357 SVR                                  0.01
160.5s 1358 QuantileRegressor                    0.10
160.5s 1359 Lars                                 0.01
160.5s 1360 NuSVR                                0.01
160.5s 1361 DummyRegressor                       0.01
160.5s 1362 LinearSVR                            0.01
160.5s 1363 MLPRegressor                         0.13
160.5s 1364 LGBMRegressor                        0.03
160.5s 1365 HistGradientBoostingRegressor        0.06
160.5s 1366 KernelRidge                          0.01
160.5s 1367 LEARNING RATE: 0.1
160.5s 1368 0%|          | 0/42 [00:00<?, ?it/s]  5%|▍         | 2/42 [00:00<00:02, 19.17it/s] 17%|█▋        | 7/42 [00:00<00:00, 35.63it/s] 26%|██▌       | 11/42 [00:00<00:01, 30.46it/s] 36%|███▌      | 15/42 [00:00<00:01, 25.32it/s] 48%|████▊     | 20/42 [00:00<00:00, 30.66it/s] 62%|██████▏   | 26/42 [00:00<00:00, 30.52it/s] 76%|███████▌  | 32/42 [00:01<00:00, 31.94it/s] 86%|████████▌ | 36/42 [00:01<00:00, 25.82it/s] 98%|█████████▊| 41/42 [00:01<00:00, 18.36it/s]100%|██████████| 42/42 [00:01<00:00, 23.89it/s]
160.6s 1369 Better model found at epoch 0 with _rmse value: 462.6142578125.
160.6s 1370 No improvement since epoch 0: early stopping
161.1s 1371 XGBoost Predictions vs Actual==========
161.1s 1372 actual  predicted
161.1s 1373 0  340.00     310.00
161.1s 1374 1   82.00      90.52
161.1s 1375 2  368.00     342.12
161.1s 1376 3  301.00     309.89
161.1s 1377 4  715.00     626.46
161.1s 1378 XGBoost RMSE:  35.589043
162.3s 1379 feature  importance
162.3s 1380 0                        GDP (current US$)       543.00
162.3s 1381 1             GDP per capita (current US$)        31.00
162.3s 1382 2                     GDP growth (annual %)      295.00
162.3s 1383 3  Imports of goods and services (% of GDP)      150.00
162.3s 1384 4  Exports of goods and services (% of GDP)      102.00
170.2s 1385 /opt/conda/lib/python3.7/site-packages/traitlets/traitlets.py:2758: FutureWarning: --Exporter.preprocessors=["remove_papermill_header.RemovePapermillHeader"] for containers is deprecated in traitlets 5.0. You can pass `--Exporter.preprocessors item` ... multiple times to add items to a list.
170.2s 1386 FutureWarning,
170.2s 1387 [NbConvertApp] Converting notebook __notebook__.ipynb to notebook
171.0s 1388 [NbConvertApp] Writing 7500347 bytes to __notebook__.ipynb
173.7s 1389 /opt/conda/lib/python3.7/site-packages/traitlets/traitlets.py:2758: FutureWarning: --Exporter.preprocessors=["nbconvert.preprocessors.ExtractOutputPreprocessor"] for containers is deprecated in traitlets 5.0. You can pass `--Exporter.preprocessors item` ... multiple times to add items to a list.
173.7s 1390 FutureWarning,
173.7s 1391 [NbConvertApp] Converting notebook __notebook__.ipynb to html
175.1s 1392 [NbConvertApp] Support files will be in __results___files/
175.1s 1393 [NbConvertApp] Making directory __results___files
175.1s 1394 [NbConvertApp] Making directory __results___files
175.1s 1395 [NbConvertApp] Making directory __results___files
175.1s 1396 [NbConvertApp] Making directory __results___files
175.1s 1397 [NbConvertApp] Making directory __results___files
175.1s 1398 [NbConvertApp] Making directory __results___files
175.1s 1399 [NbConvertApp] Making directory __results___files
175.1s 1400 [NbConvertApp] Making directory __results___files
175.1s 1401 [NbConvertApp] Making directory __results___files
175.1s 1402 [NbConvertApp] Making directory __results___files
175.1s 1403 [NbConvertApp] Making directory __results___files
175.1s 1404 [NbConvertApp] Writing 6076893 bytes to __results__.html