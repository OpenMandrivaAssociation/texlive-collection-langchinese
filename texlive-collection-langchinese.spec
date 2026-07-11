%global tl_name collection-langchinese
%global tl_revision 79450

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Chinese
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-langchinese
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langchinese.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(arphic)
Requires:	texlive(arphic-ttf)
Requires:	texlive(asymptote-by-example-zh-cn)
Requires:	texlive(asymptote-faq-zh-cn)
Requires:	texlive(asymptote-manual-zh-cn)
Requires:	texlive(cns)
Requires:	texlive(collection-langcjk)
Requires:	texlive(exam-zh)
Requires:	texlive(fandol)
Requires:	texlive(fduthesis)
Requires:	texlive(gbt9704)
Requires:	texlive(hanzibox)
Requires:	texlive(hyphen-chinese)
Requires:	texlive(impatient-cn)
Requires:	texlive(install-latex-guide-zh-cn)
Requires:	texlive(latex-notes-zh-cn)
Requires:	texlive(lshort-chinese)
Requires:	texlive(luatex-cn)
Requires:	texlive(lxgw-fonts)
Requires:	texlive(nanicolle)
Requires:	texlive(njurepo)
Requires:	texlive(pgfornament-han)
Requires:	texlive(qyxf-book)
Requires:	texlive(sjtutex)
Requires:	texlive(suanpan-l3)
Requires:	texlive(texlive-zh-cn)
Requires:	texlive(texproposal)
Requires:	texlive(tlmgr-intro-zh-cn)
Requires:	texlive(upzhkinsoku)
Requires:	texlive(xpinyin)
Requires:	texlive(xtuthesis)
Requires:	texlive(zhlineskip)
Requires:	texlive(zhlipsum)
Requires:	texlive(zhmetrics)
Requires:	texlive(zhmetrics-uptex)
Requires:	texlive(zhnumber)
Requires:	texlive(zhspacing)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Support for Chinese; additional packages in collection-langcjk.

