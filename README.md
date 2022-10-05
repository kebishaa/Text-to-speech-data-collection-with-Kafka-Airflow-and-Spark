# Data Engineering: text-to-speech data collection with Kafka, Airflow, and Spark

<img title="kafka" alt="Alt text" src="/images/collect.png" width= "1000">

<details close>
<summary><b>Business Need</b></summary>
<br>
Recognizing the value of large data sets for speech-t0-text data sets, and seeing the opportunity that there are many text corpuses for Amharic and Swahili languages, this project aims to design and build a robust, large scale, fault tolerant, highly available Kafka cluster that can be used to post a sentence and receive an audio file. 

By the end of this project, we will produce a tool that can be deployed to process posting and receiving text and audio files from and into a data lake, apply transformation in a distributed manner, and load it into a warehouse in a suitable format to train a speech-t0-text model.  

</details>
<details close>
<summary><b>Data</b></summary>
<br>
The purpose of the project is to build a data engineering pipeline that allows recording millions of Amharic and Swahili speakers reading digital texts in-app and web platforms. There are a number of large text corpora we will use, but for the purpose of testing the backend development, we can use the recently released Amharic news text classification dataset with baseline performance dataset: [IsraelAbebe/An-Amharic-News-Text-classification-Dataset: An Amharic News Text classification Dataset (github.com)](https://github.com/IsraelAbebe/An-Amharic-News-Text-classification-Dataset).

Read a brief description of the data [here](https://arxiv.org/pdf/2103.05639.pdf).

### Alternative data 
Ready-made Amharic data collected from different sources [here](https://drive.google.com/file/d/1_YLX27TdACjIF1iu8e3t-kkTb1qBlLkO/view?usp=sharing). 

</details>
<details close>
<summary><b>Technology stack</b></summary>
<br>
Integration between tools towards the final goal

<img title="kafka" alt="Alt text" src="/images/kafka.PNG">

</details>

### ___________________________________________________________________________________________
# INSTALLATION
 * git clone https://github.com/Amanuel3065/pharmaceutical_sales_prediction
 * cd pharmaceutical_sales_prediction
 * pip install -r requirements.txt **

### ___________________________________________________________________________________________
# Deployment link
 *  
### ___________________________________________________________________________________________
## Contributors
- [**Tegisty Hailay (Lead)**](https://github.com/tigisthailay)
- [**Kibatu Woldemariam**](https://github.com/kebishaa)
- [Michael Getachew](https://github.com/michaelgetachew-abebe)
- [Josias Ounsinli](https://github.com/Josias-Ounsinli)
- [Genet Shanko](https://github.com/gshanko125298).   
- [Amanuel Zewdu](https://github.com/Amanuel3065)

