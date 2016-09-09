# supertools
emci superlog tools

## instalation
1. Python2 or python3 have to be installed
2. Copy all files to directory under `$PATH`, files without extension should be executable.
3. Windows - some `.bat` wrappers are needed. Ask, or DIY and share in github

## usage
All scripts have `--help` switch

## example

    supersplit -vn50000 -s .log super cvtpem??.super*
    
joins all superlogs maching pattern `cvtpem??.super*`, then splits it into superlogs `superNNNNN.log` of 50k records each

    supergrep amt cvtpem??.super* | superwc

counts logrecords containing pattern `amt`
