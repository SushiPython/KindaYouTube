const ytdl = require('ytdl-core');
const express = require('express');
const cors = require('cors')
const app = express();

app.use(cors())

function getResult(id) {
    const result = ytdl.getInfo(id)
    console.log(result)
    return result
}

app.get('/id/:id', (req, res) => {
    console.log(req.params.id)
    getResult(req.params.id)
    .then(value => {
        console.log(value.videoDetails.title)
        res.send({
            url: value.formats[0].url,
            title: value.videoDetails.title,
            views: value.videoDetails.viewCount,
            author: value.videoDetails.author.name,
            uploaded: value.videoDetails.uploadDate
        })
    })
});

app.listen(3050, () => {
  console.log('server started');
});
