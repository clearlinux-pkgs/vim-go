Name     : vim-go
Version  : 1.18
Release  : 9
URL      : https://github.com/fatih/vim-go/archive/v1.18.tar.gz
Source0  : https://github.com/fatih/vim-go/archive/v1.18.tar.gz
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
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/vim/vim81
cp -ar {autoload,compiler,doc,ftdetect,ftplugin,indent,plugin,syntax,templates} \
    %{buildroot}/usr/share/vim/vim81

%files
%defattr(-,root,root,-)
/usr/share/vim/vim81/autoload/ctrlp/decls.vim
/usr/share/vim/vim81/autoload/fzf/decls.vim
/usr/share/vim/vim81/autoload/go/alternate.vim
/usr/share/vim/vim81/autoload/go/asmfmt.vim
/usr/share/vim/vim81/autoload/go/cmd.vim
/usr/share/vim/vim81/autoload/go/cmd_test.vim
/usr/share/vim/vim81/autoload/go/complete.vim
/usr/share/vim/vim81/autoload/go/config.vim
/usr/share/vim/vim81/autoload/go/coverage.vim
/usr/share/vim/vim81/autoload/go/debug.vim
/usr/share/vim/vim81/autoload/go/decls.vim
/usr/share/vim/vim81/autoload/go/def.vim
/usr/share/vim/vim81/autoload/go/def_test.vim
/usr/share/vim/vim81/autoload/go/doc.vim
/usr/share/vim/vim81/autoload/go/fillstruct.vim
/usr/share/vim/vim81/autoload/go/fillstruct_test.vim
/usr/share/vim/vim81/autoload/go/fmt.vim
/usr/share/vim/vim81/autoload/go/fmt_test.vim
/usr/share/vim/vim81/autoload/go/guru.vim
/usr/share/vim/vim81/autoload/go/guru_test.vim
/usr/share/vim/vim81/autoload/go/iferr.vim
/usr/share/vim/vim81/autoload/go/impl.vim
/usr/share/vim/vim81/autoload/go/impl_test.vim
/usr/share/vim/vim81/autoload/go/import.vim
/usr/share/vim/vim81/autoload/go/issue.vim
/usr/share/vim/vim81/autoload/go/job.vim
/usr/share/vim/vim81/autoload/go/jobcontrol.vim
/usr/share/vim/vim81/autoload/go/keyify.vim
/usr/share/vim/vim81/autoload/go/lint.vim
/usr/share/vim/vim81/autoload/go/lint_test.vim
/usr/share/vim/vim81/autoload/go/list.vim
/usr/share/vim/vim81/autoload/go/package.vim
/usr/share/vim/vim81/autoload/go/path.vim
/usr/share/vim/vim81/autoload/go/play.vim
/usr/share/vim/vim81/autoload/go/rename.vim
/usr/share/vim/vim81/autoload/go/statusline.vim
/usr/share/vim/vim81/autoload/go/tags.vim
/usr/share/vim/vim81/autoload/go/tags_test.vim
/usr/share/vim/vim81/autoload/go/template.vim
/usr/share/vim/vim81/autoload/go/term.vim
/usr/share/vim/vim81/autoload/go/term_test.vim
/usr/share/vim/vim81/autoload/go/test-fixtures/cmd/bad.go
/usr/share/vim/vim81/autoload/go/test-fixtures/def/jump.go
/usr/share/vim/vim81/autoload/go/test-fixtures/fmt/hello.go
/usr/share/vim/vim81/autoload/go/test-fixtures/fmt/hello_golden.go
/usr/share/vim/vim81/autoload/go/test-fixtures/fmt/imports/goimports.go
/usr/share/vim/vim81/autoload/go/test-fixtures/fmt/imports/goimports_golden.go
/usr/share/vim/vim81/autoload/go/test-fixtures/fmt/imports/vendor/gh.com/gi/foo-logging/logger.go
/usr/share/vim/vim81/autoload/go/test-fixtures/fmt/src/imports
/usr/share/vim/vim81/autoload/go/test-fixtures/lint/src/foo/foo.go
/usr/share/vim/vim81/autoload/go/test-fixtures/lint/src/lint/lint.go
/usr/share/vim/vim81/autoload/go/test-fixtures/lint/src/lint/quux.go
/usr/share/vim/vim81/autoload/go/test-fixtures/lint/src/vet/vet.go
/usr/share/vim/vim81/autoload/go/test-fixtures/tags/add_all_golden.go
/usr/share/vim/vim81/autoload/go/test-fixtures/tags/add_all_input.go
/usr/share/vim/vim81/autoload/go/test-fixtures/tags/remove_all_golden.go
/usr/share/vim/vim81/autoload/go/test-fixtures/tags/remove_all_input.go
/usr/share/vim/vim81/autoload/go/test-fixtures/term/term.go
/usr/share/vim/vim81/autoload/go/test-fixtures/test/.gitignore
/usr/share/vim/vim81/autoload/go/test-fixtures/test/src/compilerror/compilerror.go
/usr/share/vim/vim81/autoload/go/test-fixtures/test/src/play/mock/controller.go
/usr/share/vim/vim81/autoload/go/test-fixtures/test/src/play/play_test.go
/usr/share/vim/vim81/autoload/go/test-fixtures/test/src/showname/showname_test.go
/usr/share/vim/vim81/autoload/go/test-fixtures/test/src/testcompilerror/testcompilerror_test.go
/usr/share/vim/vim81/autoload/go/test-fixtures/test/src/timeout/timeout_test.go
/usr/share/vim/vim81/autoload/go/test-fixtures/test/src/veterror/veterror.go
/usr/share/vim/vim81/autoload/go/test.vim
/usr/share/vim/vim81/autoload/go/test_test.vim
/usr/share/vim/vim81/autoload/go/textobj.vim
/usr/share/vim/vim81/autoload/go/tool.vim
/usr/share/vim/vim81/autoload/go/tool_test.vim
/usr/share/vim/vim81/autoload/go/ui.vim
/usr/share/vim/vim81/autoload/go/util.vim
/usr/share/vim/vim81/autoload/gotest.vim
/usr/share/vim/vim81/autoload/unite/sources/decls.vim
/usr/share/vim/vim81/compiler/go.vim
/usr/share/vim/vim81/doc/vim-go.txt
/usr/share/vim/vim81/ftdetect/gofiletype.vim
/usr/share/vim/vim81/ftplugin/asm.vim
/usr/share/vim/vim81/ftplugin/go.vim
/usr/share/vim/vim81/ftplugin/go/commands.vim
/usr/share/vim/vim81/ftplugin/go/mappings.vim
/usr/share/vim/vim81/ftplugin/go/snippets.vim
/usr/share/vim/vim81/ftplugin/go/tagbar.vim
/usr/share/vim/vim81/ftplugin/gohtmltmpl.vim
/usr/share/vim/vim81/indent/go.vim
/usr/share/vim/vim81/indent/gohtmltmpl.vim
/usr/share/vim/vim81/plugin/go.vim
/usr/share/vim/vim81/syntax/go.vim
/usr/share/vim/vim81/syntax/godebugoutput.vim
/usr/share/vim/vim81/syntax/godebugstacktrace.vim
/usr/share/vim/vim81/syntax/godebugvariables.vim
/usr/share/vim/vim81/syntax/godefstack.vim
/usr/share/vim/vim81/syntax/gohtmltmpl.vim
/usr/share/vim/vim81/syntax/gotexttmpl.vim
/usr/share/vim/vim81/syntax/vimgo.vim
/usr/share/vim/vim81/templates/hello_world.go
/usr/share/vim/vim81/templates/hello_world_test.go
