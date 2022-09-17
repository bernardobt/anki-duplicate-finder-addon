# Duplicate Finder Config

## Variables

Change these variables to fit desired behaviour, based on your collection

- ### **shortcut**: single item

  - _Sets the shortcut that you want to use to trigger the search_
  - Example:

    "Ctrl+Shift+F6"

- ### **fieldIfNoHighlight**: single item

  - _Sets the default field that will be used as a base to search for duplicates in case nothing is highlighted in the reviewer_
  - Example:

    "Focus"

- ### **decksToCheck**: list of items

  - _Sets which deck you want to look for a duplicate_
  - Examples:

    ["first deck"]

    ["first deck", "second deck"]

- ### **fieldsToCheck**: list of items

  - _Sets with field from each card to check for a duplicate_
  - Examples:

    ["Focus"]

    ["Focus", "Expression"]

- ### **customTag**: single item

  - _Sets what will be the tag to add to the duplicate card, so you can search the duplicate card on browser_
  - Example:

    "addonFoundDuplicate"

### It's important that you respect notations:

- Don't remove the [ ] even if your list has only one item.
- Items in list must be separated by a comma.
- All items, inside a list or as a single item, must be inside quotation marks.

### **Note**

_Make sure you have a backup of your collection before making any changes in notes. The actions performed by this addon are irreversible._

_THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE._
