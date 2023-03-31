Name:		texlive-savefnmark
Version:	15878
Release:	2
Summary:	Save name of the footnote mark for reuse
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/savefnmark
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/savefnmark.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/savefnmark.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/savefnmark.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Sometimes the same footnote applies to more than one location
in a table. With this package the mark of a footnote can be
saved into a name, and re-used subsequently without creating
another footnote at the bottom.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/savefnmark/savefnmark.sty
%doc %{_texmfdistdir}/doc/latex/savefnmark/savefnmark.pdf
#- source
%doc %{_texmfdistdir}/source/latex/savefnmark/savefnmark.drv
%doc %{_texmfdistdir}/source/latex/savefnmark/savefnmark.dtx
%doc %{_texmfdistdir}/source/latex/savefnmark/savefnmark.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
