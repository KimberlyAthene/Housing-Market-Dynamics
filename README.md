# Housing Market Dynamics

Mira Antolovich, Kimberly Pierce, Houtan Rasouli, and Donatien Toni

1. DESCRIPTION

	DOC: This folder contains the final report and poster for Team 127's project "Housing Market Dynamics" 

	CODE: This folder contains all the code necessary for our dashboard to be run on a local device. Important files include:

		+main-final.html: This is the main page of our dashboard. It contains a choropleth used for selecting
					which state the user chooses for more specific information, a line chart to show historic
					trends with the most important factors by state, and a dropdown to select a SARIMA prediction
					for housing prices in 2024. From this page in the top right corner, the user can also access 
					the stats and info pages.

		+stats-final.html: This page is for a more thorough understanding of the analysis our team performed on the housing data.
					It also contains links to Wikipedia articles to better explain the performance measures
					for users who may not be as familiar with terms such as MSE or R-squared. Again, users can 
					navigate to the main or info pages in the top right corner.

		+info-final.html: This page contains our project poster as well as links to our data sources and our literature survey. 
					Users can also go back to the main and stats pages with the same navigation as the previous
					two pages.

2. INSTALLATION

	1. In order to run a demo of our code, first confirm you have installed Flask web service and Flask CORS on your device, or 
	   install them using the following commands:

			pip install -U Flask
			pip install -U flask-cors
	
	2. Once confirmed, open a Command Prompt, navigate to the folder that contains all the files, and run the following command:

			python app.py

		+This will start a local web server, typically at http://localhost:5000

	3. From a second Command Prompt, navigate to the same folder as before, and create a local host: 

			python -m http.server 8000

	4. Next, open a browser and go to http://localhost:8000/

	5. From the directory, select 'main-final.html' and this will take you to the main page of our dashboard.

3. EXECUTION

	6. From the main page, select a state in the map in order to see the historic trends for the state from 2000 - 2020. 
	   After selecting the state, a dropdown will also appear on the right that will allow the user to choose a metro area for our
	   SARIMA model. This graph should pop up after a couple of seconds and show the predicted housing price for 2024 in that area.

	7. To look at another metro area, the user can change their selection within the dropdown and the graph will reset.

	8. To look at a different state, the user can click anywhere within the map to reset it and reselect a state by clicking again. 
	   The line chart with historic trends and the dropdown will change per state and metro area.

	9. For more information about the models and analysis for our project, use the link in the top right corner to the Stats page.

	10. For our project poster, data, or literature survey, use the link in the top right corner to the Info page. 

4. DEMO VIDEO

	https://youtu.be/q5A6hsf2mwU
