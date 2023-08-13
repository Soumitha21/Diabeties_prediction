{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "27d5165a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "d=pd.read_csv(\"C:\\\\Users\\\\soumi\\\\.ipython\\\\archive (6).zip\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b2a912e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
      "0              6      148             72             35        0  33.6   \n",
      "1              1       85             66             29        0  26.6   \n",
      "2              8      183             64              0        0  23.3   \n",
      "3              1       89             66             23       94  28.1   \n",
      "4              0      137             40             35      168  43.1   \n",
      "..           ...      ...            ...            ...      ...   ...   \n",
      "763           10      101             76             48      180  32.9   \n",
      "764            2      122             70             27        0  36.8   \n",
      "765            5      121             72             23      112  26.2   \n",
      "766            1      126             60              0        0  30.1   \n",
      "767            1       93             70             31        0  30.4   \n",
      "\n",
      "     DiabetesPedigreeFunction  Age  Outcome  \n",
      "0                       0.627   50        1  \n",
      "1                       0.351   31        0  \n",
      "2                       0.672   32        1  \n",
      "3                       0.167   21        0  \n",
      "4                       2.288   33        1  \n",
      "..                        ...  ...      ...  \n",
      "763                     0.171   63        0  \n",
      "764                     0.340   27        0  \n",
      "765                     0.245   30        0  \n",
      "766                     0.349   47        1  \n",
      "767                     0.315   23        0  \n",
      "\n",
      "[768 rows x 9 columns]\n"
     ]
    }
   ],
   "source": [
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f94bd581",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>6</td>\n",
       "      <td>148</td>\n",
       "      <td>72</td>\n",
       "      <td>35</td>\n",
       "      <td>0</td>\n",
       "      <td>33.6</td>\n",
       "      <td>0.627</td>\n",
       "      <td>50</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>66</td>\n",
       "      <td>29</td>\n",
       "      <td>0</td>\n",
       "      <td>26.6</td>\n",
       "      <td>0.351</td>\n",
       "      <td>31</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8</td>\n",
       "      <td>183</td>\n",
       "      <td>64</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>23.3</td>\n",
       "      <td>0.672</td>\n",
       "      <td>32</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>89</td>\n",
       "      <td>66</td>\n",
       "      <td>23</td>\n",
       "      <td>94</td>\n",
       "      <td>28.1</td>\n",
       "      <td>0.167</td>\n",
       "      <td>21</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>137</td>\n",
       "      <td>40</td>\n",
       "      <td>35</td>\n",
       "      <td>168</td>\n",
       "      <td>43.1</td>\n",
       "      <td>2.288</td>\n",
       "      <td>33</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
       "0            6      148             72             35        0  33.6   \n",
       "1            1       85             66             29        0  26.6   \n",
       "2            8      183             64              0        0  23.3   \n",
       "3            1       89             66             23       94  28.1   \n",
       "4            0      137             40             35      168  43.1   \n",
       "\n",
       "   DiabetesPedigreeFunction  Age  Outcome  \n",
       "0                     0.627   50        1  \n",
       "1                     0.351   31        0  \n",
       "2                     0.672   32        1  \n",
       "3                     0.167   21        0  \n",
       "4                     2.288   33        1  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1ba1b2de",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>763</th>\n",
       "      <td>10</td>\n",
       "      <td>101</td>\n",
       "      <td>76</td>\n",
       "      <td>48</td>\n",
       "      <td>180</td>\n",
       "      <td>32.9</td>\n",
       "      <td>0.171</td>\n",
       "      <td>63</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>764</th>\n",
       "      <td>2</td>\n",
       "      <td>122</td>\n",
       "      <td>70</td>\n",
       "      <td>27</td>\n",
       "      <td>0</td>\n",
       "      <td>36.8</td>\n",
       "      <td>0.340</td>\n",
       "      <td>27</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>765</th>\n",
       "      <td>5</td>\n",
       "      <td>121</td>\n",
       "      <td>72</td>\n",
       "      <td>23</td>\n",
       "      <td>112</td>\n",
       "      <td>26.2</td>\n",
       "      <td>0.245</td>\n",
       "      <td>30</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>766</th>\n",
       "      <td>1</td>\n",
       "      <td>126</td>\n",
       "      <td>60</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>30.1</td>\n",
       "      <td>0.349</td>\n",
       "      <td>47</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>767</th>\n",
       "      <td>1</td>\n",
       "      <td>93</td>\n",
       "      <td>70</td>\n",
       "      <td>31</td>\n",
       "      <td>0</td>\n",
       "      <td>30.4</td>\n",
       "      <td>0.315</td>\n",
       "      <td>23</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
       "763           10      101             76             48      180  32.9   \n",
       "764            2      122             70             27        0  36.8   \n",
       "765            5      121             72             23      112  26.2   \n",
       "766            1      126             60              0        0  30.1   \n",
       "767            1       93             70             31        0  30.4   \n",
       "\n",
       "     DiabetesPedigreeFunction  Age  Outcome  \n",
       "763                     0.171   63        0  \n",
       "764                     0.340   27        0  \n",
       "765                     0.245   30        0  \n",
       "766                     0.349   47        1  \n",
       "767                     0.315   23        0  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9668b2c9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>3.845052</td>\n",
       "      <td>120.894531</td>\n",
       "      <td>69.105469</td>\n",
       "      <td>20.536458</td>\n",
       "      <td>79.799479</td>\n",
       "      <td>31.992578</td>\n",
       "      <td>0.471876</td>\n",
       "      <td>33.240885</td>\n",
       "      <td>0.348958</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>3.369578</td>\n",
       "      <td>31.972618</td>\n",
       "      <td>19.355807</td>\n",
       "      <td>15.952218</td>\n",
       "      <td>115.244002</td>\n",
       "      <td>7.884160</td>\n",
       "      <td>0.331329</td>\n",
       "      <td>11.760232</td>\n",
       "      <td>0.476951</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.078000</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>99.000000</td>\n",
       "      <td>62.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>27.300000</td>\n",
       "      <td>0.243750</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>117.000000</td>\n",
       "      <td>72.000000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>30.500000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>0.372500</td>\n",
       "      <td>29.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>6.000000</td>\n",
       "      <td>140.250000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>127.250000</td>\n",
       "      <td>36.600000</td>\n",
       "      <td>0.626250</td>\n",
       "      <td>41.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>17.000000</td>\n",
       "      <td>199.000000</td>\n",
       "      <td>122.000000</td>\n",
       "      <td>99.000000</td>\n",
       "      <td>846.000000</td>\n",
       "      <td>67.100000</td>\n",
       "      <td>2.420000</td>\n",
       "      <td>81.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Pregnancies     Glucose  BloodPressure  SkinThickness     Insulin  \\\n",
       "count   768.000000  768.000000     768.000000     768.000000  768.000000   \n",
       "mean      3.845052  120.894531      69.105469      20.536458   79.799479   \n",
       "std       3.369578   31.972618      19.355807      15.952218  115.244002   \n",
       "min       0.000000    0.000000       0.000000       0.000000    0.000000   \n",
       "25%       1.000000   99.000000      62.000000       0.000000    0.000000   \n",
       "50%       3.000000  117.000000      72.000000      23.000000   30.500000   \n",
       "75%       6.000000  140.250000      80.000000      32.000000  127.250000   \n",
       "max      17.000000  199.000000     122.000000      99.000000  846.000000   \n",
       "\n",
       "              BMI  DiabetesPedigreeFunction         Age     Outcome  \n",
       "count  768.000000                768.000000  768.000000  768.000000  \n",
       "mean    31.992578                  0.471876   33.240885    0.348958  \n",
       "std      7.884160                  0.331329   11.760232    0.476951  \n",
       "min      0.000000                  0.078000   21.000000    0.000000  \n",
       "25%     27.300000                  0.243750   24.000000    0.000000  \n",
       "50%     32.000000                  0.372500   29.000000    0.000000  \n",
       "75%     36.600000                  0.626250   41.000000    1.000000  \n",
       "max     67.100000                  2.420000   81.000000    1.000000  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3e0c6b40",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 768 entries, 0 to 767\n",
      "Data columns (total 9 columns):\n",
      " #   Column                    Non-Null Count  Dtype  \n",
      "---  ------                    --------------  -----  \n",
      " 0   Pregnancies               768 non-null    int64  \n",
      " 1   Glucose                   768 non-null    int64  \n",
      " 2   BloodPressure             768 non-null    int64  \n",
      " 3   SkinThickness             768 non-null    int64  \n",
      " 4   Insulin                   768 non-null    int64  \n",
      " 5   BMI                       768 non-null    float64\n",
      " 6   DiabetesPedigreeFunction  768 non-null    float64\n",
      " 7   Age                       768 non-null    int64  \n",
      " 8   Outcome                   768 non-null    int64  \n",
      "dtypes: float64(2), int64(7)\n",
      "memory usage: 54.1 KB\n"
     ]
    }
   ],
   "source": [
    "d.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "2dd6c555",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(768, 9)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "65795fcd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pregnancies                 0\n",
       "Glucose                     0\n",
       "BloodPressure               0\n",
       "SkinThickness               0\n",
       "Insulin                     0\n",
       "BMI                         0\n",
       "DiabetesPedigreeFunction    0\n",
       "Age                         0\n",
       "Outcome                     0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4e4a9513",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "no.of rows 768\n",
      "no.of columns 9\n"
     ]
    }
   ],
   "source": [
    "print(\"no.of rows\",d.shape[0])\n",
    "print(\"no.of columns\",d.shape[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "32c96eb4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d7f6b90e",
   "metadata": {},
   "outputs": [],
   "source": [
    "copy=d.copy(deep=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "49d5b723",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',\n",
       "       'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "92c6b233",
   "metadata": {},
   "outputs": [],
   "source": [
    "copy[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',\n",
    "       'BMI']]=copy[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',\n",
    "       'BMI']].replace(0,np.nan)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "17b8d640",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pregnancies                   0\n",
       "Glucose                       5\n",
       "BloodPressure                35\n",
       "SkinThickness               227\n",
       "Insulin                     374\n",
       "BMI                          11\n",
       "DiabetesPedigreeFunction      0\n",
       "Age                           0\n",
       "Outcome                       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "copy.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b1a89f9d",
   "metadata": {},
   "outputs": [],
   "source": [
    "d['Glucose']=d['Glucose'].replace(0,d['Glucose'].mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "b71aabe2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0      148.0\n",
      "1       85.0\n",
      "2      183.0\n",
      "3       89.0\n",
      "4      137.0\n",
      "       ...  \n",
      "763    101.0\n",
      "764    122.0\n",
      "765    121.0\n",
      "766    126.0\n",
      "767     93.0\n",
      "Name: Glucose, Length: 768, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "print(d['Glucose'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "cfe96485",
   "metadata": {},
   "outputs": [],
   "source": [
    "d['BloodPressure']=d['BloodPressure'].replace(0,d['BloodPressure'].mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c65d0e0e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0      72.0\n",
      "1      66.0\n",
      "2      64.0\n",
      "3      66.0\n",
      "4      40.0\n",
      "       ... \n",
      "763    76.0\n",
      "764    70.0\n",
      "765    72.0\n",
      "766    60.0\n",
      "767    70.0\n",
      "Name: BloodPressure, Length: 768, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "print(d['BloodPressure'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "fd6e4a6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "d['SkinThickness']=d['SkinThickness'].replace(0,d['SkinThickness'].mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "3ba059a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0      35.000000\n",
      "1      29.000000\n",
      "2      20.536458\n",
      "3      23.000000\n",
      "4      35.000000\n",
      "         ...    \n",
      "763    48.000000\n",
      "764    27.000000\n",
      "765    23.000000\n",
      "766    20.536458\n",
      "767    31.000000\n",
      "Name: SkinThickness, Length: 768, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "print(d['SkinThickness'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "96b88fcd",
   "metadata": {},
   "outputs": [],
   "source": [
    "d['Insulin']=d['Insulin'].replace(0,d['Insulin'].mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "6fad6b9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "d['BMI']=d['BMI'].replace(0,d['BMI'].mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "fdfb98cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0      33.6\n",
      "1      26.6\n",
      "2      23.3\n",
      "3      28.1\n",
      "4      43.1\n",
      "       ... \n",
      "763    32.9\n",
      "764    36.8\n",
      "765    26.2\n",
      "766    30.1\n",
      "767    30.4\n",
      "Name: BMI, Length: 768, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "print(d['BMI'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "390e131b",
   "metadata": {},
   "outputs": [],
   "source": [
    "X=d.drop('Outcome',axis=1)\n",
    "y=d['Outcome']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "964a2095",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>6</td>\n",
       "      <td>148.0</td>\n",
       "      <td>72.0</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>79.799479</td>\n",
       "      <td>33.6</td>\n",
       "      <td>0.627</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>85.0</td>\n",
       "      <td>66.0</td>\n",
       "      <td>29.000000</td>\n",
       "      <td>79.799479</td>\n",
       "      <td>26.6</td>\n",
       "      <td>0.351</td>\n",
       "      <td>31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8</td>\n",
       "      <td>183.0</td>\n",
       "      <td>64.0</td>\n",
       "      <td>20.536458</td>\n",
       "      <td>79.799479</td>\n",
       "      <td>23.3</td>\n",
       "      <td>0.672</td>\n",
       "      <td>32</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>89.0</td>\n",
       "      <td>66.0</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>94.000000</td>\n",
       "      <td>28.1</td>\n",
       "      <td>0.167</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>137.0</td>\n",
       "      <td>40.0</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>168.000000</td>\n",
       "      <td>43.1</td>\n",
       "      <td>2.288</td>\n",
       "      <td>33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>763</th>\n",
       "      <td>10</td>\n",
       "      <td>101.0</td>\n",
       "      <td>76.0</td>\n",
       "      <td>48.000000</td>\n",
       "      <td>180.000000</td>\n",
       "      <td>32.9</td>\n",
       "      <td>0.171</td>\n",
       "      <td>63</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>764</th>\n",
       "      <td>2</td>\n",
       "      <td>122.0</td>\n",
       "      <td>70.0</td>\n",
       "      <td>27.000000</td>\n",
       "      <td>79.799479</td>\n",
       "      <td>36.8</td>\n",
       "      <td>0.340</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>765</th>\n",
       "      <td>5</td>\n",
       "      <td>121.0</td>\n",
       "      <td>72.0</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>112.000000</td>\n",
       "      <td>26.2</td>\n",
       "      <td>0.245</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>766</th>\n",
       "      <td>1</td>\n",
       "      <td>126.0</td>\n",
       "      <td>60.0</td>\n",
       "      <td>20.536458</td>\n",
       "      <td>79.799479</td>\n",
       "      <td>30.1</td>\n",
       "      <td>0.349</td>\n",
       "      <td>47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>767</th>\n",
       "      <td>1</td>\n",
       "      <td>93.0</td>\n",
       "      <td>70.0</td>\n",
       "      <td>31.000000</td>\n",
       "      <td>79.799479</td>\n",
       "      <td>30.4</td>\n",
       "      <td>0.315</td>\n",
       "      <td>23</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>768 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Pregnancies  Glucose  BloodPressure  SkinThickness     Insulin   BMI  \\\n",
       "0              6    148.0           72.0      35.000000   79.799479  33.6   \n",
       "1              1     85.0           66.0      29.000000   79.799479  26.6   \n",
       "2              8    183.0           64.0      20.536458   79.799479  23.3   \n",
       "3              1     89.0           66.0      23.000000   94.000000  28.1   \n",
       "4              0    137.0           40.0      35.000000  168.000000  43.1   \n",
       "..           ...      ...            ...            ...         ...   ...   \n",
       "763           10    101.0           76.0      48.000000  180.000000  32.9   \n",
       "764            2    122.0           70.0      27.000000   79.799479  36.8   \n",
       "765            5    121.0           72.0      23.000000  112.000000  26.2   \n",
       "766            1    126.0           60.0      20.536458   79.799479  30.1   \n",
       "767            1     93.0           70.0      31.000000   79.799479  30.4   \n",
       "\n",
       "     DiabetesPedigreeFunction  Age  \n",
       "0                       0.627   50  \n",
       "1                       0.351   31  \n",
       "2                       0.672   32  \n",
       "3                       0.167   21  \n",
       "4                       2.288   33  \n",
       "..                        ...  ...  \n",
       "763                     0.171   63  \n",
       "764                     0.340   27  \n",
       "765                     0.245   30  \n",
       "766                     0.349   47  \n",
       "767                     0.315   23  \n",
       "\n",
       "[768 rows x 8 columns]"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "7ac8f553",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0      1\n",
       "1      0\n",
       "2      1\n",
       "3      0\n",
       "4      1\n",
       "      ..\n",
       "763    0\n",
       "764    0\n",
       "765    0\n",
       "766    1\n",
       "767    0\n",
       "Name: Outcome, Length: 768, dtype: int64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "eb6eeaef",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "bbe377a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "3f965a6b",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.svm import SVC\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.ensemble import GradientBoostingClassifier\n",
    "from sklearn.pipeline import Pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "c54ed8d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "pipeline_lr=Pipeline([('scalar1',StandardScaler()),('lr_classifier',LogisticRegression())])\n",
    "pipeline_knn=Pipeline([('scalar2',StandardScaler()),('knn_classifier',KNeighborsClassifier())])\n",
    "pipeline_svc=Pipeline([('scalar3',StandardScaler()),('svc_classifier',SVC())])\n",
    "pipeline_dt=Pipeline([('dt_classifier',DecisionTreeClassifier())])\n",
    "pipeline_rf=Pipeline([('rf_classifier',RandomForestClassifier(max_depth=3))])\n",
    "pipeline_gb=Pipeline([('gb_classifier',GradientBoostingClassifier())])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "9cfd8b2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "pipelines=[pipeline_lr,pipeline_knn,pipeline_svc,pipeline_dt,pipeline_rf,pipeline_gb]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "e9419c62",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Pipeline(steps=[('scalar1', StandardScaler()),\n",
       "                 ('lr_classifier', LogisticRegression())]),\n",
       " Pipeline(steps=[('scalar2', StandardScaler()),\n",
       "                 ('knn_classifier', KNeighborsClassifier())]),\n",
       " Pipeline(steps=[('scalar3', StandardScaler()), ('svc_classifier', SVC())]),\n",
       " Pipeline(steps=[('dt_classifier', DecisionTreeClassifier())]),\n",
       " Pipeline(steps=[('rf_classifier', RandomForestClassifier(max_depth=3))]),\n",
       " Pipeline(steps=[('gb_classifier', GradientBoostingClassifier())])]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pipelines"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "fab8e667",
   "metadata": {},
   "outputs": [],
   "source": [
    "for pipe in pipelines:\n",
    "    pipe.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "8d254e24",
   "metadata": {},
   "outputs": [],
   "source": [
    "pipe_dict={0:'LR',1:'KNN',2:'SVC',3:'DT',4:'RF',5:'GB'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "d5d7eaaf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{0: 'LR', 1: 'KNN', 2: 'SVC', 3: 'DT', 4: 'RF', 5: 'GB'}"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pipe_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "d42ea13a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LR test accuracy : 76.62337662337663\n",
      "KNN test accuracy : 76.62337662337663\n",
      "SVC test accuracy : 73.37662337662337\n",
      "DT test accuracy : 74.02597402597402\n",
      "RF test accuracy : 77.27272727272727\n",
      "GB test accuracy : 75.97402597402598\n"
     ]
    }
   ],
   "source": [
    "for i,model in enumerate(pipelines):\n",
    "    print(\"{} test accuracy : {}\".format(pipe_dict[i],model.score(X_test,y_test)*100))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "97fcd677",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier(max_depth=3)"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X=d.drop('Outcome',axis=1)\n",
    "y=d['Outcome']\n",
    "rf=RandomForestClassifier(max_depth=3)\n",
    "rf.fit(X,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "34358524",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Pregnancies  Glucose  BloodPressure  SkinThickness    Insulin   BMI  \\\n",
      "0            6    148.0           72.0           35.0  79.799479  33.6   \n",
      "\n",
      "   DiabetesPedigreeFunction  Age  \n",
      "0                     0.627   50  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "new_data = pd.DataFrame({'Pregnancies': [6], \n",
    "                         'Glucose': [148.0], \n",
    "                         'BloodPressure': [72.0], \n",
    "                         'SkinThickness': [35.0], \n",
    "                         'Insulin': [79.799479], \n",
    "                         'BMI': [33.6], \n",
    "                         'DiabetesPedigreeFunction': [0.627], \n",
    "                         'Age': [50]})\n",
    "\n",
    "print(new_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "febcf379",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1]\n"
     ]
    }
   ],
   "source": [
    "rf.predict(new_data)\n",
    "p=rf.predict(new_data)\n",
    "print(p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "9ed64173",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Diabetic\n"
     ]
    }
   ],
   "source": [
    "if p[0]==0:\n",
    "    print('Non-Diabetic')\n",
    "else:   \n",
    "    print(\"Diabetic\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "a4673acb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "c0ad9736",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['model_joblib_diabetes']"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "joblib.dump(rf,'model_joblib_diabetes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "be0efde5",
   "metadata": {},
   "outputs": [],
   "source": [
    "model=joblib.load('model_joblib_diabetes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "593be6bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1], dtype=int64)"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.predict(new_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "2015177f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#GUI\n",
    "\n",
    "from tkinter import *\n",
    "import joblib\n",
    "import numpy as np\n",
    "from sklearn import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "500ce18b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def show_entry_fields():\n",
    "    p1=float(e1.get())\n",
    "    p2=float(e2.get())\n",
    "    p3=float(e3.get())\n",
    "    p4=float(e4.get())\n",
    "    p5=float(e5.get())\n",
    "    p6=float(e6.get())\n",
    "    p7=float(e7.get())\n",
    "    p8=float(e8.get())\n",
    "    \n",
    "    model=joblib.load('model_joblib_diabetes')    \n",
    "    result=model.preict([[p1,p2,p3,p4,p5,p6,p7,p8]])\n",
    "    \n",
    "    if result==0:\n",
    "        Label(master,text='Non-diabetic').grid(row=31)\n",
    "    else:\n",
    "         Label(master,text='diabetic').grid(row=31)\n",
    "            \n",
    "master=Tk()\n",
    "master.title('Diabetes prediction using machine learning')\n",
    "\n",
    "\n",
    "label=Label(master,text='Diabetes prediction using machine learning', bg='black',fg='white').grid(row=0,columnspan=2)\n",
    "\n",
    "Label(master,text='Pregnancies').grid(row=1)\n",
    "Label(master,text='Glucose').grid(row=2)\n",
    "Label(master,text='BloodPressure').grid(row=3)\n",
    "Label(master,text='SkinThickness').grid(row=4)\n",
    "Label(master,text='Insulin').grid(row=5)\n",
    "Label(master,text='BMI').grid(row=6)\n",
    "Label(master,text='DiabetesPedigreeFunction').grid(row=7)\n",
    "Label(master,text='Age').grid(row=8)\n",
    "\n",
    "e1=Entry(master)\n",
    "e2=Entry(master)\n",
    "e3=Entry(master)\n",
    "e4=Entry(master)\n",
    "e5=Entry(master)\n",
    "e6=Entry(master)\n",
    "e7=Entry(master)\n",
    "e8=Entry(master)\n",
    "\n",
    "e1.grid(row=1,column=1)\n",
    "e2.grid(row=2,column=1)\n",
    "e3.grid(row=3,column=1)\n",
    "e4.grid(row=4,column=1)\n",
    "e5.grid(row=5,column=1)\n",
    "e6.grid(row=6,column=1)\n",
    "e7.grid(row=7,column=1)\n",
    "e8.grid(row=8,column=1)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df05dab8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
