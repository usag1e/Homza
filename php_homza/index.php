<?php
	require_once 'lib/couch.php';
	require_once 'lib/couchClient.php';
	require_once 'lib/couchDocument.php';
	require_once 'lib/dataAccess.php';

	$view1 = last_seen();
	$view_img = get_url_img();
	$view_house=get_printer_status();
	//$view_temperature=get_temperature():

	
include('includes/header.php');
echo "<meta http-equiv='refresh' content='120;url=http://127.0.0.1/php_homza'>";
	
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
	<?php
		echo "SSID : Torrieux " ;
		echo "&nbsp;&nbsp;&nbsp;&nbsp;";
		echo " Pwd : 4J3E8A7NBRILLANT";
	?>	
	</head>
	
<body>
    <div id="page">
    <div>
	<h2> Who's UP ? </h2><br />
			<?php
				
				foreach ( $view_img->rows as $row){
					$date =  $row->key;
					$url_img =  $row->value;
					$nowdate = time();
					$timestamp = strtotime($date);
					$seen_since = $nowdate - $timestamp;
					if ($seen_since < 300){
						echo '<div class="img_in" style="background-image:url('.$url_img[1].')"></div>';	
					}elseif ($seen_since < 900){
						echo '<div class="img_just
" style="background-image:url('.$url_img[1].')"></div>';
					}else {
						echo '<div class="img_out" style="background-image:url('.$url_img[1].')"></div>';
					}
				}		
			?>
    </div>
    <div>
	<h2> Last Seen </h2><br />
			<?php
				foreach ( $view1->rows as $row ){	
					$word = $row->value;
					$date = $row->key;
					$nowdate = time();
					$timestamp = strtotime($date);
					$seen_since = $nowdate - $timestamp;
					$nowdate = gmdate("Y-m-d H:i", $nowdate);
					$newDate = date("Y-m-d H:i", strtotime($date));
					if ($last_seen_since<$seen_since){
						$last_seen_since=$seen_since;
						$last_recordman=$word;
					}

					if ($seen_since < 300){
						echo '<a href="detail_word.php?word='.$word.'">'.$word.'</a> : In da House ! ( '.secondsToTime($seen_since).' )';
					}elseif ($seen_since <900){
						echo '<a href="detail_word.php?word='.$word.'">'.$word.'</a> : Should be around ... (less than 15 minutes ago)';
					}else {
						echo '<a href="detail_word.php?word='.$word.'">'.$word.'</a> : Out ! - '.secondsToTime($seen_since).' ago ( '.$newDate.' )';
					}
				echo ' - RECORD : '.$last_seen_since.' sec <br/>';
				}
			?>

	</div>
	<div>
		<h2> Weather </h2><br />
			<?php
				$json = "http://127.0.0.1:5984/house_status/_design/list/_view/weather";
				$jsonfile = file_get_contents($json);

				$weather = json_decode($jsonfile);
				echo 'Temperature is : ' , $weather->rows[2]->key, ' Celsius <br />';
				echo 'Pressure is : ' , $weather->rows[2]->value,'<br />';
			?>
			
	</div>		
	<div>
	<h2> Octoprint </h2><br />

			<?php
				$json = "http://127.0.0.1:5984/house_status/_design/list/_view/printer";
				$jsonfile = file_get_contents($json);
		$printer_json = json_decode($jsonfile);
				echo ' <b>Printer is currently </b> :  ', $printer_json->rows[0]->value->printer_status;
				echo '<br /> <b>Head temperature</b> :  ', $printer_json->rows[0]->value->head_temperature;
				echo '<br /> <b>Bed temperature</b> :  ', $printer_json->rows[0]->value->bed_temperature;
				echo '<br /> <b>Job name </b> : ', $printer_json->rows[0]->value->job_name;
				
			?>
			
    	
    
	</div>
</div>
</body>
</html>
