# Sound Sieve Worker
## Purpose
Free up web resources by queuing long-running work, and receiving them here, where source separation is applied.

## System Design
<table>
   <tr>
      <td><h5>↓</h5><br>Poll SQS for messages<br><br><h5>↓</h5><br>Process sequentially<br><br><h5>↓</h5><br>Upload stems to S3<br><br><h5>↓</h5><br>Send notification upon completion.
      </td>
      <td>
         <p align="center">
            <img src='img/soundsieveworkersystemdesign.png' style='width:415px' />
         </p>
      </td>
   </tr>
</table>


## Business Logic
1. `uri`   ⃪ pop off S3 audio file uri from SQS
1. `file`   ⃪ download `uri` to memory
1. `stem1, stem2,…, stemN`   ⃪ `spleeter.separator.Separator.separate(file)`
1. `user.uploadURI.stemsURI`   ⃪ s3.upload('stem1', 'stem2',…, 'stemN')


