<?php
$name = $_POST['name'];
$visiotor_email = ˘$_POST['email'];
$message = $_POST['message'];

$email_from = 'vidkuralt.github.io';
$email_subject = "New Form Submission";
$email_body = "User Name:" $name.\n".
				"User Email: $visiotor_email.\n".
				    "User Message: $message.\n".
					
$to = "kuraltvid@gmail.com";
$headers = "From: $email_from \r\n";
$headers .= "Reply-To: $visitor_email \r\n";
mail($to,&email_subject,$email_body,$headers);
header("Location: contact.html");
 
?>