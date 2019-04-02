# Hackathon Timer App

Tag: #HTML #CSS #JS #CountDownTimer #Hackathon #AWS #S3 #ReinventTheWheel

As we got ready to kick start the Reinvent the wheel Hackathon, the team prepared everything from the challenge, eye masks, catering, playlist, networking, live leaderboard, and the whole nine yards. However when the time came to display a 24 Hr count down timer in the big screen, We couldn't find a decent, minimal, clutter-free Count down timer in the web without ads.  

Here is the pretty basic HTML/CSS/JS code to build a minimal Count Down Timer. App is deployed in AWS S3 bucket, it is as simple as creating a static hosting bucket and uploading the index.html. You could quickly change the logo, color scheme, fonts to match your need and taste. 

Link to the App : http://hackathon-timer.s3-website-us-east-1.amazonaws.com/

### Setup Timer 

Update Line 77
```
var countDownDate = new Date("Mar 27, 2020 17:00:00").getTime();
```

### Clock Color
Update Line 54
```
.clock {
    transform: translateY(22vh);
    color: orangered;
    font-size: 4vh;
}
```

### Logo/Heading Text
Update Line 68
```
<clock>
    <div>
        <p class="logo">Reinvent The Wheel 2.0</p>
        <p class="clock" id="timer"></p>
    </div>
</clock>
```

[Code Pen](https://codepen.io/ravishan16/pen/KYdppM)

### Deploy to AWS S3

1. Create an S3 Bucket (URL will be http://<Bucket-Name>.s3-website-<Region>.amazonaws.com/) and the bucket names should be globally unique
 
2. Set Properties 
3. Update Bucket Policy
   ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AddPerm",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::<Bucket Name>/*"
            }
        ]
    }
   ```
4. Upload/Sync code to the bucker (Use awscli)
   ```
    aws s3 cp index.html s3://hackathon-timer/
   ```