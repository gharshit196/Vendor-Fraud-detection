{/* <html>
    <head>
        <title>DataViz</title>
        <style type="text/css">
            #viz {
                width: 900px;
                height: 700px;
            }
        </style>
        <script src="https://rawgit.com/neo4j-contrib/neovis.js/master/dist/neovis.js"></script>
    </head>   
    <script>
        function draw() {
            var config = {
                container_id: "viz",
                server_url: "bolt://3.210.183.118:7687",
                server_user: "neo4j",
                server_password: "documents-bias-relocations",
                labels: {
                    "Troll": {
                        caption: "user_key",
                        size: "pagerank",
                        community: "community"
                    }
                },
                relationships: {
                    "RETWEETS": {
                        caption: false,
                        thickness: "count"
                    }
                },
                initial_cypher: "MATCH p=(:Troll)-[:RETWEETS]->(:Troll) RETURN p"
            }

            var viz = new NeoVis.default(config);
            viz.render();
        }
    </script>
    <body onload="draw()">
        <div id="viz"></div>
    </body>
</html> */}