# Team 
Lucie Svobodová **xsvobo1x**

Jakub Kuzník **xkuzni04**

Adam Kaňkovský **xkanko00**

## Earned points 
### Part 1: Storing Extensive Data in NoSQL Databases.
**8/8**
### Part 2 Data Preparation and Their Descriptive Characteristics.
**8/8**
### Part 3 Data Extraction from the Web.
**8/8**


## Assignment Part 1: Storing Extensive Data in NoSQL Databases.

**The aim of this part of the project is** to analyze the requirements and design the optimal way to store extensive data in a suitable NoSQL database so that this data can be quickly queried and updated.


**The solution to this part consists of several steps:**
1. Based on lectures and exercises in the subject, study the characteristics and usage possibilities of various types of NoSQL databases, specifically:
   - Wide-column databases (e.g., Apache Cassandra)
   - Document databases (e.g., MongoDB)
   - Graph databases (e.g., Neo4J)
   - Time-series databases (e.g., InfluxDB)

2. Study the available datasets in the National Open Data Catalog for the statutory city of Brno, with a particular focus on specific datasets from this source. Examine their structure (schema), types of data items, identifiers, possibilities of linking datasets (common entities), connections to external data (other sources, real-world entities), changes in data over time (updates), and more.


3. For each of the above-mentioned types of NoSQL databases, find a dataset from the datasets mentioned above that would be suitable for storage and querying in that specific type of NoSQL database (and not in another). In total, you will use at least 4 different datasets for 4 different types of NoSQL databases. Specifically, for each individual case, describe:

    - The full name of the selected dataset, including the URL link in the above-mentioned catalog.
    - The suitable distribution of the dataset (e.g., CSV or GeoJSON) as per the catalog's offerings.
    - The chosen type of NoSQL database and a specific database product/server (e.g., Apache Cassandra).
    - A detailed and logical explanation of why it is best to use the chosen type of NoSQL database for storing and querying the selected dataset (compared to other types of NoSQL databases). The explanation must be specific to the dataset and database and should refer to their specific characteristic features, such as columns (structure/schema, data types, domain sizes, etc.), rows (count, size, diversity, existence of identifiers and references, etc.), data creation and storage process (source, update frequency and period, data reliability/error rate, possibility of retroactive changes to already published data or only adding new data, compression and aggregation possibilities, data retention/forgetting, distribution and scalability of the storage, redundancy, etc.), data consumption process (predefined and ad-hoc queries, frequency and period of result retrieval, distribution and scalability of data processing for queries, the position of result consumers in relation to the location and processing of data, possibilities for query acceleration using caching/pre-computation, indexing possibilities, etc.).
    - (Note: This translation is a direct conversion of the provided text into English. The content appears to describe a complex data analysis task and may require further context to fully understand and implement.)
    - Syntactically and semantically correct commands for defining storage in a given product/server of a NoSQL database for the selected dataset (schema definition in CQL, example document insertion in JavaScript, importing nodes and relationships in Cypher, etc., based on the chosen database server).
    - Algorithmic description of data import from the chosen distribution of the dataset into the prepared database, including both the initial population of an empty database with data and subsequent updates of new or modified data (focus on selecting and using an appropriate record key in NoSQL to enable UPSERT based on it, rather than inserting duplicate records; deleting all data in the database and reinserting them is not allowed). You can submit a short script (e.g., in Python) or describe the chosen algorithm steps in pseudocode or text.
    - At least one syntactically and semantically correct query in the language of the selected database product over the data stored in the database for the chosen dataset. This query should demonstrate the suitability of the chosen type of NoSQL database for the given data, including a description of how the database server will respond (how it will locate nodes where the requested data is stored, retrieve data from nodes, process it in a distributed manner, deliver results to the client who initiated the query, and how the client will consume the results).

4. Verify and discuss within the team the suitability of the selected dataset, the correctness of the chosen type of NoSQL database, the usability, and the complexity of the described data loading method into the database, as well as the execution of queries in the database, and the correctness of all commands or queries (it is essential to practically test the commands and queries on datasets and database products to ensure their correctness).

5. Record the required results in a structured document or supplement with scripts or examples in files referenced in the document. Package them into a ZIP archive and submit them through the VUT information system (IS VUT).

**As part of the project, only the results are submitted without defense. Therefore, it is necessary to submit appropriate documentation so that compliance with the assignment can be assessed based on it.**

### Assignment Part 2 Data Preparation and Their Descriptive Characteristics.
tbd
### Assignmetn Part 3 Data Extraction from the Web.
tbd
