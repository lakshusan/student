---
toc: false
comments: false
layout: post
title: Tables of Data
description: A table of data based on one of my interests, books!
courses: {compsci: {week: 3}}
type: hacks
---

### Markdown Table
Google [markdown cheat sheet](https://www.markdownguide.org/extended-syntax/#tables) and it lead you to an outline for how to make a table.

| Book Series | Release Year | Total Pages |
|------|-------|------|-------|-------|
|Harry Potter|1997|4,224|
|Champ Half Blood Chronicles|2005|11,102|
|Wings of Fire|2012|5,020|
|Land of Stories|2012|2,896|
|Keeper of the Lost Cities|2012|7,009|
|The School for Good and Evil|2013|3,760|


### HTML Table
First listed is code for the HTML table, then the output.


```python
%%html

<h2>HTML Cell Output from Jupyter</h2>

<!-- Body contains the contents of the Document -->
<body>
    <table class="table">
        <thead>
            <tr>
                <th>Book Series</th>
                <th>Release Year</th>
                <th>Total Pages</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Harry Potter</td>
                <td>1997</td>
                <td>4,224</td>
            </tr>
            <tr>
                <td>Camp Half Blood Chronicles</td>
                <td>2005</td>
                <td>11,102</td>
            </tr>
            <tr>
                <td>Wings of Fire</td>
                <td>2012</td>
                <td>5,020</td>
            </tr>
            <tr>
                <td>Land of Stories</td>
                <td>2012</td>
                <td>2,896</td>
            </tr>
            <tr>
                <td>Keeper of the Lost Cities</td>
                <td>2012</td>
                <td>7,009</td>
            </tr>
            <tr>
                <td>The School for Good and Evil</td>
                <td>2013</td>
                <td>2,760</td>
            </tr>
        </tbody>
    </table>
</body>
```


<h3>HTML Cell Output from Jupyter</h3>

<!-- Body contains the contents of the Document -->
<body>
    <table class="table">
        <thead>
            <tr>
                <th>Book Series</th>
                <th>Release Year</th>
                <th>Total Pages</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Harry Potter</td>
                <td>1997</td>
                <td>4,224</td>
            </tr>
            <tr>
                <td>Camp Half Blood Chronicles</td>
                <td>2005</td>
                <td>11,102</td>
            </tr>
            <tr>
                <td>Wings of Fire</td>
                <td>2012</td>
                <td>5,020</td>
            </tr>
            <tr>
                <td>Land of Stories</td>
                <td>2012</td>
                <td>2,896</td>
            </tr>
            <tr>
                <td>Keeper of the Lost Cities</td>
                <td>2012</td>
                <td>7,009</td>
            </tr>
            <tr>
                <td>The School for Good and Evil</td>
                <td>2013</td>
                <td>2,760</td>
            </tr>
        </tbody>
    </table>
</body>



## HTML Table in Markdown Cell with JavaScript jquery
JavaScript is a programming language that works with HTML data, CSS helps to style that data.  In this example, we are using JavaScript and CSS that was developed by others (3rd party).  Addithing the 3rd party code makes the table interactive.
- Look at the href and src on lines inside of the lines in `<head>` tags.  This is adding code to our page from others.
- Observe the `<script>` tags at the bottom of the page.  This is generating the interactive table, from the third party code, using the data `<table id="demo">` from the `<body>`.  

<!-- Head contains information to Support the Document -->
<head>
    <!-- load jQuery and DataTables output style and scripts -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>var define = null;</script>
    <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
</head>

<!-- Body contains the contents of the Document -->
<body>
    <table id="md_demo" class="table">
        <thead>
            <tr>
                <th>Make</th>
                <th>Model</th>
                <th>Year</th>
                <th>Color</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Ford</td>
                <td>Mustang</td>
                <td>2022</td>
                <td>Red</td>
                <td>$35,000</td>
            </tr>
            <tr>
                <td>Toyota</td>
                <td>Camry</td>
                <td>2022</td>
                <td>Silver</td>
                <td>$25,000</td>
            </tr>
            <tr>
                <td>Tesla</td>
                <td>Model S</td>
                <td>2022</td>
                <td>White</td>
                <td>$80,000</td>
            </tr>
            <tr>
                <td>Cadillac</td>
                <td>Broughan</td>
                <td>1969</td>
                <td>Black</td>
                <td>$10,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>F-350</td>
                <td>1997</td>
                <td>Green</td>
                <td>$15,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>Excursion</td>
                <td>2003</td>
                <td>Green</td>
                <td>$25,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>Ranger</td>
                <td>2012</td>
                <td>Red</td>
                <td>$8,000</td>
            </tr>
            <tr>
                <td>Kuboto</td>
                <td>L3301 Tractor</td>
                <td>2015</td>
                <td>Orange</td>
                <td>$12,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>Fusion Energi</td>
                <td>2015</td>
                <td>Guard</td>
                <td>$25,000</td>
            </tr>
            <tr>
                <td>Acura</td>
                <td>XL</td>
                <td>2006</td>
                <td>Grey</td>
                <td>$10,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>F150 Lightning</td>
                <td>2024</td>
                <td>Guard</td>
                <td>$70,000</td>
            </tr>
        </tbody>
    </table>
</body>

<!-- Script is used to embed executable code -->
<script>
    $("#md_demo").DataTable();
</script>


## Hacks
This lesson teaches you about tables.  In this hack, it is important that you analze the difference in the styles of output shown.  
- Make your own tables, with data according to your interests.
- Describe a benefit of a markdown table.
- Try to Style the HTML table using w3schools.
- Describe the difference between HTML and JavaScript.
- Describe a benefit of a table that uses JavaScript.