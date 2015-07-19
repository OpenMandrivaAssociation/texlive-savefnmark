# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/savefnmark
# catalog-date 2007-01-14 15:20:52 +0100
# catalog-license gpl
# catalog-version 1.0
Name:		texlive-savefnmark
Version:	1.0
Release:	10
Summary:	Save name of the footnote mark for reuse
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/savefnmark
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/savefnmark.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/savefnmark.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/savefnmark.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755793
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719484
- texlive-savefnmark
- texlive-savefnmark
- texlive-savefnmark
- texlive-savefnmark

