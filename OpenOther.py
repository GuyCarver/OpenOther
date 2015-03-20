#----------------------------------------------------------------------
# Copyright (c) 2013, Guy Carver
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright notice,
#       this list of conditions and the following disclaimer in the documentation
#       and/or other materials provided with the distribution.
#
#     * The name of Guy Carver may not be used to endorse or promote products # derived#
#       from # this software without specific prior written permission.#
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# FILE    OpenOther.py
# BY      Guy Carver
# DATE    06/08/2013 08:48 PM
#----------------------------------------------------------------------

import sublime, sublime_plugin
import os.path

class OpenOtherCommand(sublime_plugin.WindowCommand):
  def run( self ) :
    vw = self.window.active_view()
    if not vw.is_scratch() :
      fname = vw.file_name()
      if fname :
        #Read the extensions setting from the view.
        exts = vw.settings().get("extensions")
        if exts :
          # print("checking " + str(exts))
          #Get the extension of the current file.
          fpath, fext = os.path.splitext(fname)
          if fext :
            fext = fext[1:] #Get rid of the '.'.
            # print("looking for " + fext)
            if fext in exts :
              exts.remove(fext)

          def good( aEntry ) :
            fname = fpath + '.' + aEntry
            return os.path.exists(fname)

          items = [ x for x in exts if good(x) ]

          def done( index ) :
            if index >= 0 :
              fname = fpath + '.' + items[index]
              self.window.open_file(fname)

          l = len(items)
          if l > 1:
#            def preview( index ) :
#              if index >= 0:
#                fname = fpath + '.' + items[index]
#                self.window.open_file(fname, sublime.TRANSIENT)

            #open a selection prompt
            self.window.show_quick_panel(items, done)
          elif l :
            done(0)

#class OpenOtherCommand(sublime_plugin.WindowCommand):
#  def run( self ) :
#    vw = self.window.active_view()
#    if not vw.is_scratch() :
#      fname = vw.file_name()
#      if fname :
#        #Read the extensions setting from the view.
#        exts = vw.settings().get("extensions")
#        if exts :
#          # print("checking " + str(exts))
#          #Get the extension of the current file.
#          fpath, fext = os.path.splitext(fname)
#          if fext :
#            fext = fext[1:] #Get rid of the '.'.
#            # print("looking for " + fext)
#            if fext in exts :
#              index = exts.index(fext)
#
#              def iterexts( aList ) :
#                for testext in aList :
#                  # print("checking " + testext)
#                  fname = fpath + '.' + testext
#                  if os.path.exists(fname):
#                    # print("found " + fname)
#                    if self.window.open_file(fname) :
#                      return True
#                return False
#
#              #Search from this point to end.
#              if index < len(exts) - 1 :
#                if iterexts(exts[index + 1:]) :
#                  return
#
#              #Search from this point to beginning.
#              if index > 0 :
#                if iterexts(exts[:index]) :
#                   return
