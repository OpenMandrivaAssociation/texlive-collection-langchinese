# revision 33790
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langchinese
Version:	20140621
Release:	4
Summary:	Chinese
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langchinese.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-langcjk
Requires:	texlive-arphic
Requires:	texlive-cns
Requires:	texlive-ctex
Requires:	texlive-ctex-faq
Requires:	texlive-fandol
Requires:	texlive-hyphen-chinese
Requires:	texlive-latex-notes-zh-cn
Requires:	texlive-lshort-chinese
Requires:	texlive-texlive-zh-cn
Requires:	texlive-xpinyin
Requires:	texlive-zhmetrics
Requires:	texlive-zhnumber
Requires:	texlive-zhspacing

%description
Support for Chinese; additional packages in collection-langcjk.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
