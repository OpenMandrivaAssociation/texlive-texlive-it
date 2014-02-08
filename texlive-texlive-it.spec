# revision 26875
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-it
Version:	20120808
Release:	2
Summary:	TeX Live manual (Italian)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-it.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-it.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive texlive-it package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdir}/doc/texlive/texlive-it/Makefile
%doc %{_texmfdir}/doc/texlive/texlive-it/texlive-it.html
%doc %{_texmfdir}/doc/texlive/texlive-it/texlive-it.pdf
%doc %{_texmfdir}/doc/texlive/texlive-it/texlive-it.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120808-1
+ Revision: 812904
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 756634
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719697
- texlive-texlive-it
- texlive-texlive-it
- texlive-texlive-it
- texlive-texlive-it

