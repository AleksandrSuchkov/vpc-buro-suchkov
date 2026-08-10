import io,os,sys
S='/private/tmp/claude-501/-Users-admin-Projects-pager-sashi-suchkova/1dbb82ad-7a31-4f7d-a3e5-7ddfca3af5a4/scratchpad/'
OUT='/Users/admin/Projects/Девелопмент/VPC Бюро Сучкова/leads/diagnostika-promo.html'
src=open(S+'promo-src.html',encoding='utf-8').read()
fonts=open(S+'tt-travels-fonts.css',encoding='utf-8').read().strip()
motion=open(S+'mbuild/motion-bundle.js',encoding='utf-8').read().strip()
mark=open(S+'logo-mark.svg',encoding='utf-8').read().strip()
for name,val in (('/*__FONTS__*/',fonts),('/*__MOTION__*/',motion),('/*__MARK__*/',mark)):
    assert src.count(name)==1, '%s встречается %d раз'%(name,src.count(name))
    src=src.replace(name,val,1)
assert '</script' not in motion and '<!--' not in motion, 'бандл небезопасен для инлайна'
open(OUT,'w',encoding='utf-8').write(src)
print('собрано: %s' % OUT)
print('размер: %d байт (%.0f КБ)' % (len(src.encode()), len(src.encode())/1024))
import gzip; print('в gzip: %.0f КБ' % (len(gzip.compress(src.encode()))/1024))
