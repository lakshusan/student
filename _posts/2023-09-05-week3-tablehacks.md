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

The third-party code adds a few features you cannot get without it; It adds the search bar and allows you to change the order of the table on the site.

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
                <th>Book Series</th>
                <th>Release Year</th>
                <th>Number of Pages</th>
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
                <td>The School For Good and Evil</td>
                <td>2013</td>
                <td>2,760</td>
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