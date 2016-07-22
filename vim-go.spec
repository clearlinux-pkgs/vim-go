Name     : vim-go
Version  : 1.7.1
Release  : 1
URL      : https://github.com/fatih/vim-go/archive/v1.7.1.tar.gz
Source0  : https://github.com/fatih/vim-go/archive/v1.7.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause

%description
# vim-go
Go (golang) support for Vim, which comes with pre-defined sensible settings (like
auto gofmt on save), with autocomplete, snippet support, improved syntax
highlighting, go toolchain commands, and more.  If needed vim-go installs all
necessary binaries for providing seamless Vim integration with current
commands. It's highly customizable and each individual feature can be
disabled/enabled easily.

%prep
%setup -q -n vim-go-1.7.1

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/vim/vim74
cp -ar {autoload,compiler,doc,ftdetect,ftplugin,indent,plugin,syntax} \
    %{buildroot}/usr/share/vim/vim74

%files
%defattr(-,root,root,-)
/usr/share/vim/vim74/autoload/ctrlp/decls.vim
/usr/share/vim/vim74/autoload/go/alternate.vim
/usr/share/vim/vim74/autoload/go/asmfmt.vim
/usr/share/vim/vim74/autoload/go/cmd.vim
/usr/share/vim/vim74/autoload/go/complete.vim
/usr/share/vim/vim74/autoload/go/coverage.vim
/usr/share/vim/vim74/autoload/go/def.vim
/usr/share/vim/vim74/autoload/go/doc.vim
/usr/share/vim/vim74/autoload/go/fmt.vim
/usr/share/vim/vim74/autoload/go/guru.vim
/usr/share/vim/vim74/autoload/go/impl.vim
/usr/share/vim/vim74/autoload/go/import.vim
/usr/share/vim/vim74/autoload/go/jobcontrol.vim
/usr/share/vim/vim74/autoload/go/lint.vim
/usr/share/vim/vim74/autoload/go/list.vim
/usr/share/vim/vim74/autoload/go/package.vim
/usr/share/vim/vim74/autoload/go/path.vim
/usr/share/vim/vim74/autoload/go/play.vim
/usr/share/vim/vim74/autoload/go/rename.vim
/usr/share/vim/vim74/autoload/go/term.vim
/usr/share/vim/vim74/autoload/go/textobj.vim
/usr/share/vim/vim74/autoload/go/tool.vim
/usr/share/vim/vim74/autoload/go/ui.vim
/usr/share/vim/vim74/autoload/go/util.vim
/usr/share/vim/vim74/compiler/go.vim
/usr/share/vim/vim74/doc/vim-go.txt
/usr/share/vim/vim74/ftdetect/gofiletype.vim
/usr/share/vim/vim74/ftplugin/asm.vim
/usr/share/vim/vim74/ftplugin/go.vim
/usr/share/vim/vim74/ftplugin/go/commands.vim
/usr/share/vim/vim74/ftplugin/go/mappings.vim
/usr/share/vim/vim74/ftplugin/go/snippets.vim
/usr/share/vim/vim74/ftplugin/go/tagbar.vim
/usr/share/vim/vim74/ftplugin/gohtmltmpl.vim
/usr/share/vim/vim74/indent/go.vim
/usr/share/vim/vim74/indent/gohtmltmpl.vim
/usr/share/vim/vim74/plugin/go.vim
/usr/share/vim/vim74/syntax/go.vim
/usr/share/vim/vim74/syntax/godefstack.vim
/usr/share/vim/vim74/syntax/gohtmltmpl.vim
/usr/share/vim/vim74/syntax/gotexttmpl.vim
/usr/share/vim/vim74/syntax/vimgo.vim
