


// Get the element with class name "container"


//Please Subscribe Ash_is_Coding.

function sendOTP() {
    const email = document.getElementById('email');
    const otpverify = document.getElementsByClassName('otpverify')[0];
    // const container = document.querySelector('.container');

    // // If the element exists, hide it
    // Create a SMTP crendentials that I showed u in my previous video

    // Generating random number as OTP;(999999 - 100000 + 1)) + 100000
    let otp_val = Math.floor(Math.random() * (999999 - 100000 + 1) + 10000);

    let emailbody = `
            <h1>Please Subscribe to Ash_is_Coding</h1> <br>
            <h2>Your OTP is </h2>${otp_val}
            `;
    console.log("clicked 1..");

    Email.send({
        SecureToken: "c2972d4d-71eb-4653-be52-efd77d9ef233",
        To: 'msnithin84@gmail.com',
        From: "msnithin84@gmail.com",
        Subject: "hi otp",
        Body: emailbody
    }).then(
        //if success it returns "OK";
        message => {
            if (message === "OK") {
                alert("OTP sent to your email " + email.value);

                // now making otp input visible
                otpverify.style.display = "block";
                const otp_inp = document.getElementById('otp_inp');
                const otp_btn = document.getElementById('otp-btn');
                const btn = document.getElementById('btn');

                otp_btn.addEventListener('click', () => {
                    // now check whether sent email is valid
                    if (otp_inp.value == otp_val) {
                        alert("Email address verified...");
                        otpverify.style.display = "none";
                        btn.style.display = "none";
                        // window.location.assign('../templates/index.html');
                    }
                    else {
                        alert("Invalid OTP");
                    }
                })
            }
        }
    );

}
function mongo() {
    window.location.assign("{{ url_for( 'index' )  }}");

    // Connect to the database
    const client = new MongoClient('mongodb://localhost:27017');
    // Import the MongoDB driver
    const MongoClient = require('mongodb');
    const email = document.getElementById('email');
    const pass = document.getElementById('password');
    const name = document.getElementById('name');



    // Get the database and collection
    const db = client.db('login');
    const collection = db.collection('details');

    // Insert a document
    const document = {
        name: name.value,
        mailid: email.value,
        password: pass.value,

    };

    collection.insertOne(document, function (err, result) {
        if (err) throw err;
        alert('signin was successfully ');
        window.location.assign('../templates/index.html');
    });

    // Close the connection
    client.close();
}