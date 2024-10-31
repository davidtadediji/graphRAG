from neo4j import GraphDatabase

uri = "neo4j+ssc://e9cf9921.databases.neo4j.io"
user = "neo4j"
password = "Kn7IP_HXAxyGFF6g09lyooDxpuSyebps1ednfKqXxJA"

driver = GraphDatabase.driver(uri, auth=(user, password))
with driver.session() as session:
    result = session.run("RETURN 1")
    print(result.single())
