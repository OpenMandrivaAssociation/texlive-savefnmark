# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/savefnmark
# catalog-date 2007-01-14 15:20:52 +0100
# catalog-license gpl
# catalog-version 1.0
Name:		texlive-savefnmark
Version:	1.0
Release:	1
Summary:	Save name of the footnote mark for reuse
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/savefnmark
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/savefnmark.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/savefnmark.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/savefnmark.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Sometimes the same footnote applies to more than one location
in a table. With this package the mark of a footnote can be
saved into a name, and re-used subsequently without creating
another footnote at the bottom.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/savefnmark/savefnmark.sty
%doc %{_texmfdistdir}/doc/latex/savefnmark/savefnmark.pdf
#- source
%doc %{_texmfdistdir}/source/latex/savefnmark/savefnmark.drv
%doc %{_texmfdistdir}/source/latex/savefnmark/savefnmark.dtx
%doc %{_texmfdistdir}/source/latex/savefnmark/savefnmark.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
