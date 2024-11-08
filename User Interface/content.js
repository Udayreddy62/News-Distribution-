debugger

async function populateTable() {

    const response = await fetchData();

    const table = document.getElementById('sched-table');

 

    // Create table headers (optional)

    const headers = ['Company Name', 'Country Code','Delivery timestamp utc','Headline','Isin','Keywords','News id','Story','Ticker id','Ticker region','Topic'];

    const headerRow = table.insertRow();

    headers.forEach((header) => {

      const cell = headerRow.insertCell();

      cell.textContent = header;

    });

 

    // Populate data

   response.data.forEach(item => {

      const row = table.insertRow();

      const company_nameCell = row.insertCell();

      const country_codeCell = row.insertCell();

      const delivery_timestamp_utcCell = row.insertCell();

      const headlineCell = row.insertCell();

      const isinCell = row.insertCell();

      const keywordsCell = row.insertCell();

      const news_idCell = row.insertCell();

      const storyCell = row.insertCell();

      const ticker_idCell = row.insertCell();

      const ticker_regionCell = row.insertCell();

      const topicCell = row.insertCell();

      company_nameCell.textContent = item.company_name;

      country_codeCell.textContent = item.country_code;

      delivery_timestamp_utcCell.textContent = item.delivery_timestamp_utc;

      headlineCell.textContent = item.headline;

      isinCell.textContent = item.isin;

      keywordsCell.textContent = item.keywords;

      news_idCell.textContent = item.news_id;

      storyCell.textContent = item.story;

      ticker_idCell.textContent = item.ticker_id;

      ticker_regionCell.textContent = item.ticker_region;

      topicCell.textContent = item.topic;

     

    });

  }

 

  // Call the function to populate the table

  populateTable();

 
