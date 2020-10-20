// reqired div are selected by getElementById function
const input=document.getElementById('input');
const result=document.getElementById('result');
const result2=document.getElementById('result2');
const btn=document.getElementById('btn');
var CAPITAL;//global varriable is defined
var CURRENCY;
var EXRATE=0;
const WEATHER_APIKEY =config.weather_apikey;//api key is accessed from a config.js file
const CURRENCY_APIKEY= config.currency_apikey;
//when button is clicked api request is sent to three servers and reponse is updated to result div
btn.addEventListener('click',()=>{
  cnt_name=input.value;//searchbox value is stored in cnt_name
  const country_api=`https://restcountries.eu/rest/v2/name/${cnt_name}`;//api request is sent along with country name
  fetch(country_api)
    .then(response=>{
      return response.json();

    })
    //after getting the response name of country, capital, currency sign and namee is stored as respective varriable
    .then(data=>{
      var{name,capital}=data[0];
      CAPITAL=capital;// value of capital is initialized to global CAPITAL varriable
      const{code}=data[0].currencies[0];
      CURRENCY=code;
      const curr_name=data[0].currencies[0].name;
      console.log(name);
      console.log(capital);
      console.log(code);
      console.log(curr_name);
    })
//then api request is sent to weather api server along with capital name of country
    .then(data=>{
     const api=`https://api.openweathermap.org/data/2.5/weather?q=${CAPITAL}&appid=${WEATHER_APIKEY}`
     fetch(api)
       .then(response=>{
         return response.json();
       })
       //after getting the response back current weather information is extracted and stored in local varriable
       .then(data=>{
         const {id,main,description,icon}=data.weather[0];
         const {temp,pressure,humidity}=data.main;
         console.log(temp,pressure,humidity);
         console.log(description);
         //result div in main page is updated with weather information
         result.innerHTML=`
         <h4> ${main} ${description} </h4>
         <p> Current temp:${temp/10} degree celcius, Current pressure: ${pressure} mb, Current humidity: ${humidity}%</p>
         <img src="http://openweathermap.org/img/wn/${icon}@2x.png"/>// weather image is also updated along with other information
         `;
       });
     })
     //then api request is sent to fixer ip  server along with currency symbol of country with base symbol euro
     .then(data=>{
       const cur_api=`http://data.fixer.io/api/latest?access_key=${CURRENCY_APIKEY}&base=EUR&symbols=${CURRENCY}`
       fetch(cur_api)
       .then(response=>{
         return response.json();
       })
       //then exchange rate is updated to result 2 div in home page
       .then(data=>{
         const rate=data['rates'][CURRENCY];
         EXRATE=rate;
         console.log(rate);
         console.log(EXRATE);
         result2.innerHTML=`<p> Current exchange rate 1 EUR = ${EXRATE} ${CURRENCY} </p>`
       });
     })
});
