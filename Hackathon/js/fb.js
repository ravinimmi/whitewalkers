var graphUrl = "https://graph.facebook.com/me?" + CAAXlF8qt7UUBAGBrZBZCuJ6mNc2d2kZC4ZComskB3xWHeZAgRalssI6yXZC9zbcRYprqfejEP6i47M4xyixX2e7nh9QIc8iR0URznqs5Jpxr2xBhXvfjHjZABZCbNZBZCSflvgZAwqE5XXSMQ2HVz1qJgNOAvFYyqvE1i7H5vZCmTZAvcC9kqZBBQ4DrXz7eZBLIO0wMbZC7d41bXbyBIAZDZD + "&callback=displayUser";
console.log(graphUrl);
 
var script = document.createElement("script");
script.src = graphUrl;
document.body.appendChild(script);
 
function displayUser(user) {
    console.log(user);
}