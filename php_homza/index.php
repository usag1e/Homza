<?php
	require_once 'lib/couch.php';
	require_once 'lib/couchClient.php';
	require_once 'lib/couchDocument.php';
	require_once 'lib/dataAccess.php';

	$view1 = last_seen();

	
include('includes/header.php');
	
?><!DOCTYPE html>
<html>
	<head>
	
        <link href='http://fonts.googleapis.com/css?family=Lato:300,400' rel='stylesheet' type='text/css'>
        <link href="//netdna.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes"/>
        <link href="assets/css/icon.css" rel="stylesheet" type="text/css">
        <link href="assets/css/style.css" rel="stylesheet" type="text/css">
        
                <link rel="stylesheet" href="http://cdn.oesmith.co.uk/morris-0.5.1.css">
                <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
                <script src="//cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script>
                <script src="http://cdn.oesmith.co.uk/morris-0.5.1.min.js"></script>

	</head>
	
<body>

    <div id="page">

            <h2>Who's home?</h2>
			<?php
				foreach ( $view1->rows as $row ){
					$word = $row->value;
					$date = $row->key;
					
					$nowdate = time();
					$timestamp = strtotime($date);
					$seen_since = $nowdate - $timestamp;
					$nowdate = gmdate("Y-m-d H-i-s", $nowdate);
					
					$newDate = date("Y-m-d H-i-s", strtotime($date));
					
					echo '<a href="detail_word.php?word='.$word.'">'.$word.'</a> last seen '.$newDate.', which is '.$seen_since.' seconds ago. <br/>';

			} ?>

		

    </div>


</body>
</html>
