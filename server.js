const express = require('express')
const request = require('request')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})


const axios = require('axios')

//const axios = require('axios')

axios.post('https://localhost:5000/try', {
    "key": "1",
    "work": ["yash", "lodu", "monu"]
})
    .then(async (response) => {

        console.log(response.data.names)
    }).catch(e=>console.log(e))

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})