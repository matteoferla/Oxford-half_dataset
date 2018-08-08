## Grabbed data for the Oxford half
This data is for a question for Giuseppe. Namely, is the MET decrease seen with aging decrease different in smaller runs.
It is scraped data that is not anonymised: please don't use it.
These are my notes.

### 2012-2014
These three years are from the Oxford mail.
`.txt` is raw, `.csv` is parsed.

    import re
    for year in [2012,2013,2014]:
        bundle=open('Ox-{}.txt'.format(year),'r').read()
        with open('Ox-{}.csv'.format(year),'w') as w:
            w.write('Position, Name, Chip time\n')
            for m in re.findall('(\d+) ([\w\s\-\']+) (\d+:\d+:\d+)',bundle):
                w.write(','.join(m)+'\n')

### 2015-2016
These data can be downloaded as `xlsx` from `sporthive.com`.
That is überkind of them. Maybe future datasets?

### 2017
Not downloadable.
Potentially the dataset could be downloaded via ajax request, which has a limit and an offset. But this is the lazy way.
Modded the "See more" a-element to have the attribute `id='hack'` so that it can be handled.

    $('.vs-results__more-btn').attr('id','hack');
    $('#hack').html('READY');
    var counter=0;
    var maxc=200;
    function clicker(n) {document.getElementById('hack').click();
        if (counter < maxc) {counter++; window.setTimeout(clicker,200);}; console.log(counter);}
    clicker();

Issue when the timer is absent: double entries have the same position.
As the browser crashes out, I did it by downloading each age category. Using the command `$('.vs-result').each(function () {$(this).remove();});` did not solve the speed issue.
Copy paste fixed with:

    bundle=open('Ox-2018-over50s.txt','r').readlines()
    with open('Ox-2016-over50s.csv','w') as w:
        w.write('Rank,Name,BIB,Club or Crew,Age,Gender,Pace / Km,Chip Time\n')
        for line in bundle[1:]:
            rex=re.match('(\d+)(\D+?)(\d+)(.*?)(\d\d)(\w)(\d\d:\d\d)(\d\d:\d\d:\d\d)',line)
            if not rex:
                print('ERROR...',line)
            else:
                pass
                w.write(','.join(rex.groups())+'\n')

