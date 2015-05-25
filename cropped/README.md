# CAMS CTF 2015: Cropped

### Problem

**Points**: 150

**Description**: 

> It looks suspiciously short for an image. It almost looks cropped. Or is it?  
> cropped.jpg

**Hint**: 

None given.

### Solution

Many types of files contain metadata, or data about the file itself. We automatically run `exiftool`, a useful utility that displays EXIF metadata, on every JPEG we get. The flag is the name of the text layer.

```
[!] exiftool cropped.jpg 
ExifTool Version Number         : 9.13
File Name                       : cropped.jpg
Directory                       : .
File Size                       : 333 kB
File Modification Date/Time     : 2015:05:24 21:04:50-04:00
File Access Date/Time           : 2015:05:24 21:04:49-04:00
File Inode Change Date/Time     : 2015:05:24 21:04:57-04:00
File Permissions                : rw-r-----
File Type                       : JPEG
MIME Type                       : image/jpeg
Exif Byte Order                 : Big-endian (Motorola, MM)
Photometric Interpretation      : RGB
Orientation                     : Horizontal (normal)
Samples Per Pixel               : 3
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Software                        : Adobe Photoshop CC 2014 (Windows)
Modify Date                     : 2015:03:26 20:36:55
Exif Version                    : 0221
Color Space                     : sRGB
Exif Image Width                : 691
Exif Image Height               : 1024
Compression                     : JPEG (old-style)
Thumbnail Offset                : 398
Thumbnail Length                : 3900
Current IPTC Digest             : c75d17e574b56ef5dbbe3994c0e9795c
Coded Character Set             : UTF8
Application Record Version      : 0
IPTC Digest                     : c75d17e574b56ef5dbbe3994c0e9795c
Displayed Units X               : inches
Displayed Units Y               : inches
Global Angle                    : 30
Global Altitude                 : 30
Photoshop Thumbnail             : (Binary data 3900 bytes, use -b option to extract)
Photoshop Quality               : 12
Photoshop Format                : Standard
Progressive Scans               : 3 Scans
XMP Toolkit                     : Adobe XMP Core 5.5-c021 79.155772, 2014/01/13-19:44:00
Document ID                     : adobe:docid:photoshop:7cdf1376-d432-11e4-870c-9e09ed6b6f96
Instance ID                     : xmp.iid:40d10882-79d0-1a40-b2f8-fa8e2e57046d
Original Document ID            : C0798895E7B06DA6CF5528A60768023A
Format                          : image/jpeg
Color Mode                      : RGB
ICC Profile Name                : sRGB v1.31 (Canon)
Create Date                     : 2015:03:26 20:34:53-07:00
Metadata Date                   : 2015:03:26 20:36:55-07:00
Creator Tool                    : Adobe Photoshop CC 2014 (Windows)
History Action                  : saved, converted, derived, saved, saved, converted, derived, saved
History Instance ID             : xmp.iid:d0e899cc-8040-ab48-a7de-0999a397f40c, xmp.iid:ad5e5e38-92a0-ef49-81a9-320c753feb90, xmp.iid:d498679f-23a6-3940-b8f5-b95f2a9359d0, xmp.iid:40d10882-79d0-1a40-b2f8-fa8e2e57046d
History When                    : 2015:03:26 20:36:27-07:00, 2015:03:26 20:36:27-07:00, 2015:03:26 20:36:55-07:00, 2015:03:26 20:36:55-07:00
History Software Agent          : Adobe Photoshop CC 2014 (Windows), Adobe Photoshop CC 2014 (Windows), Adobe Photoshop CC 2014 (Windows), Adobe Photoshop CC 2014 (Windows)
History Changed                 : /, /, /, /
History Parameters              : from image/jpeg to application/vnd.adobe.photoshop, converted from image/jpeg to application/vnd.adobe.photoshop, from application/vnd.adobe.photoshop to image/jpeg, converted from application/vnd.adobe.photoshop to image/jpeg
Derived From Instance ID        : xmp.iid:d498679f-23a6-3940-b8f5-b95f2a9359d0
Derived From Document ID        : adobe:docid:photoshop:7310298c-d432-11e4-a9f7-e0f83fc15932
Derived From Original Document ID: C0798895E7B06DA6CF5528A60768023A
Text Layer Name                 : {h1dd3n_from_vew}
Text Layer Text                 : {h1dd3n_from_vew}
Profile CMM Type                : UCCM
Profile Version                 : 2.4.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2003:04:04 00:00:00
Profile File Signature          : acsp
Primary Platform                : Microsoft Corporation
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : CANO
Device Model                    : Z009
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : CANO
Profile ID                      : 0
Red Tone Reproduction Curve     : (Binary data 2060 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 2060 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 2060 bytes, use -b option to extract)
Red Matrix Column               : 0.43604 0.22244 0.0139
Green Matrix Column             : 0.3851 0.71695 0.09708
Blue Matrix Column              : 0.14307 0.06062 0.71393
Chromatic Adaptation            : 1.04784 0.02289 -0.05019 0.02954 0.99051 -0.01706 -0.00923 0.01508 0.75172
Profile Copyright               : Copyright (c) 2003, Canon Inc.  All rights reserved.
Device Mfg Desc                 : Canon Inc.
Device Model Desc               : sRGB v1.31 (Canon)
Media White Point               : 0.9642 1 0.82491
Technology                      : Cathode Ray Tube Display
Profile Description             : sRGB v1.31 (Canon)
DCT Encode Version              : 100
APP14 Flags 0                   : [14]
APP14 Flags 1                   : (none)
Color Transform                 : YCbCr
Image Width                     : 691
Image Height                    : 170
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 691x170
Thumbnail Image                 : (Binary data 3900 bytes, use -b option to extract)
```

**Flag**: `{h1dd3n_from_vew}`

### Other Resources

* [The EXIF standard](http://www.exiv2.org/Exif2-2.PDF)
