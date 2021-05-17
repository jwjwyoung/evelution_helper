# Q 0 : # Setting.plugin_sample_plugin
Query(Setting)

# Q 1 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 2 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 3 : # Project.find
Query(Project)
.where("id = ?")
# Q 4 : # version.is_a?(Version)
Query(Version)

# Q 5 : # version.is_a?
Query(Version)

# Q 6 : # tokens.empty?
Query(Token)

# Q 7 : # message.root
Query(Message)

# Q 8 : # message.root.children
Query(Message)

# Q 9 : # message.root
Query(Message)

# Q 10 : # Query.operators_by_filter_type
Query(Query)

# Q 11 : # Query.operators
Query(Query)

# Q 12 : # version.name
Query(Version)
.select('name')
# Q 13 : # User.current.role_for_project(@project)
Query(User)

# Q 14 : # User.current.role_for_project
Query(User)

# Q 15 : # User.current
Query(User)

# Q 16 : # tokens.join
Query(Token)

# Q 17 : # attachments.any?
Query(Attachment)

# Q 18 : # custom_value.custom_field
Query(CustomField)
.where("id = ?")
# Q 19 : # custom_value.custom_field
Query(CustomField)
.where("id = ?")
# Q 20 : # message.subject
Query(Message)
.select('subject')
# Q 21 : # message.board.watcher_recipients
Query(Board)
.where("id = ?")
# Q 22 : # message.board
Query(Board)
.where("id = ?")
# Q 23 : # custom_field.id
Query(CustomField)

# Q 24 : # version.project_id
Query(Version)
.select('project_id')
# Q 25 : # @document.attachments.find(:all, :order => "created_on DESC")
Query(Attachment)
.where("document_id = ?")
.where("id = ?")
# Q 26 : # @document.attachments.find(:all, :order => "created_on DESC")
Query(Attachment)
.where("document_id = ?")
.where("id = ?")
# Q 27 : # @document.attachments.find
Query(Attachment)
.where("document_id = ?")
.where("id = ?")
# Q 28 : # @document.attachments
Query(Attachment)
.where("document_id = ?")
# Q 29 : # IssueStatus.find(:all, :order => "position")
Query(IssueStatus)
.where("id = ?")
# Q 30 : # IssueStatus.find(:all, :order => "position")
Query(IssueStatus)
.where("id = ?")
# Q 31 : # IssueStatus.find
Query(IssueStatus)
.where("id = ?")
# Q 32 : # IssueRelation.new(params[:relation])
Query(IssueRelation)

# Q 33 : # IssueRelation.new(params[:relation])
Query(IssueRelation)

# Q 34 : # IssueRelation.new
Query(IssueRelation)

# Q 35 : # @project.queries.find(:all, :order => "name ASC", :conditions => ["is_public = ? or user_id = ?", true, (
# logged_in_user ? logged_in_user.id : 0)])
Query(Query)
.where("project_id = ?")
.where("id = ?")
.where("is_public = ?")
.where("user_id = ?")
.where("id = ?")
# Q 36 : # @project.queries.find(:all, :order => "name ASC", :conditions => ["is_public = ? or user_id = ?", true, (
# logged_in_user ? logged_in_user.id : 0)])
Query(Query)
.where("project_id = ?")
.where("id = ?")
.where("is_public = ?")
.where("user_id = ?")
.where("id = ?")
# Q 37 : # @project.queries.find
Query(Query)
.where("project_id = ?")
.where("id = ?")
# Q 38 : # @project.queries
Query(Query)
.where("project_id = ?")
# Q 39 : # User.current
Query(User)

# Q 40 : # User.current
Query(User)

# Q 41 : # custom_field.is_required?
Query(CustomField)

# Q 42 : # self.scm_adapter
Query(Repository)

# Q 43 : # Token.generate_token_value
Query(Token)

# Q 44 : # Token.generate_token_value
Query(Token)

# Q 45 : # custom_field.id
Query(CustomField)

# Q 46 : # user.logged?
Query(User)

# Q 47 : # version.completed?
Query(Version)

# Q 48 : # message.board_id
Query(Message)
.select('board_id')
# Q 49 : # @project.wiki
Query(Wiki)
.where("id = ?")
# Q 50 : # Wiki.new(:project => @project)
Query(Wiki)

# Q 51 : # Wiki.new
Query(Wiki)

# Q 52 : # @attachment.diskfile
Query(Attachment)

# Q 53 : # @attachment.filename
Query(Attachment)
.select('filename')
# Q 54 : # custom_field.regexp.blank?
Query(CustomField)
.select('regexp')
# Q 55 : # custom_field.regexp
Query(CustomField)
.select('regexp')
# Q 56 : # custom_field.regexp
Query(CustomField)
.select('regexp')
# Q 57 : # Setting.notified_events.include?("message_posted")
Query(Setting)

# Q 58 : # Setting.notified_events.include?
Query(Setting)

# Q 59 : # Setting.notified_events
Query(Setting)

# Q 60 : # version.name
Query(Version)
.select('name')
# Q 61 : # message.root
Query(Message)

# Q 62 : # @attachment.content_type
Query(Attachment)
.select('content_type')
# Q 63 : # @project.members
Query(Member)
.where("project_id = ?")
# Q 64 : # Member.new(params[:member])
Query(Member)

# Q 65 : # Member.new
Query(Member)

# Q 66 : # @version.update_attributes(params[:version])
Query(Version)

# Q 67 : # @version.update_attributes
Query(Version)

# Q 68 : # self.port
Query(AuthSourceLdap)
.select('port')
# Q 69 : # custom_field.min_length
Query(CustomField)
.select('min_length')
# Q 70 : # custom_field.min_length
Query(CustomField)
.select('min_length')
# Q 71 : # issue.recipients
Query(Issue)

# Q 72 : # issue.recipients
Query(Issue)

# Q 73 : # custom_field.field_format
Query(CustomField)
.select('field_format')
# Q 74 : # message.parent_id
Query(Message)
.select('parent_id')
# Q 75 : # message.id
Query(Message)

# Q 76 : # User.current.allowed_to?({ :controller => controller, :action => action }, @project)
Query(User)

# Q 77 : # User.current.allowed_to?
Query(User)

# Q 78 : # User.current
Query(User)

# Q 79 : # issue.subject
Query(Issue)
.select('subject')
# Q 80 : # @wiki.save
Query(Wiki)

# Q 81 : # @news.update_attributes(params[:news])
Query(News)

# Q 82 : # @news.update_attributes
Query(News)

# Q 83 : # @attachment.image?
Query(Attachment)

# Q 84 : # custom_field.max_length
Query(CustomField)
.select('max_length')
# Q 85 : # custom_field.max_length
Query(CustomField)
.select('max_length')
# Q 86 : # role.member?
Query(Role)

# Q 87 : # issue.project.name
Query(Project)
.where("id = ?")
.select('name')
# Q 88 : # issue.project
Query(Project)
.where("id = ?")
# Q 89 : # issue.tracker.name
Query(Tracker)
.where("id = ?")
.select('name')
# Q 90 : # issue.tracker
Query(Tracker)
.where("id = ?")
# Q 91 : # issue.id
Query(Issue)

# Q 92 : # issue.status.name
Query(IssueStatus)
.where("id = ?")
.select('name')
# Q 93 : # issue.status
Query(IssueStatus)
.where("id = ?")
# Q 94 : # issue.subject
Query(Issue)
.select('subject')
# Q 95 : # Issue.find_by_id(m[1])
Query(Issue)

# Q 96 : # Issue.find_by_id(m[1])
Query(Issue)

# Q 97 : # Issue.find_by_id
Query(Issue)

# Q 98 : # issue.project.name
Query(Project)
.where("id = ?")
.select('name')
# Q 99 : # issue.project
Query(Project)
.where("id = ?")
# Q 100 : # issue.tracker.name
Query(Tracker)
.where("id = ?")
.select('name')
# Q 101 : # issue.tracker
Query(Tracker)
.where("id = ?")
# Q 102 : # issue.id
Query(Issue)

# Q 103 : # issue.status.name
Query(IssueStatus)
.where("id = ?")
.select('name')
# Q 104 : # issue.status
Query(IssueStatus)
.where("id = ?")
# Q 105 : # issue.subject
Query(Issue)
.select('subject')
# Q 106 : # issue.start_date
Query(Issue)
.select('start_date')
# Q 107 : # Enumeration::get_values("DCAT")
Query(Enumeration)

# Q 108 : # Enumeration::get_values("DCAT")
Query(Enumeration)

# Q 109 : # Enumeration::get_values
Query(Enumeration)

# Q 110 : # Issue.table_name
Query(Issue)

# Q 111 : # User.current.logged?
Query(User)

# Q 112 : # User.current
Query(User)

# Q 113 : # User.current
Query(User)

# Q 114 : # Project.find(:all, :include => :repository)
Query(Project)
.where("id = ?")
# Q 115 : # Project.find
Query(Project)
.where("id = ?")
# Q 116 : # custom_field.field_format
Query(CustomField)
.select('field_format')
# Q 117 : # issue.due_date
Query(Issue)
.select('due_date')
# Q 118 : # @document.update_attributes(params[:document])
Query(Document)

# Q 119 : # @document.update_attributes
Query(Document)

# Q 120 : # CustomField.find(:all).group_by
Query(CustomField)
.where("id = ?")
# Q 121 : # CustomField.find(:all)
Query(CustomField)
.where("id = ?")
# Q 122 : # CustomField.find
Query(CustomField)
.where("id = ?")
# Q 123 : # @project.versions
Query(Version)
.where("project_id = ?")
# Q 124 : # Message.new(:subject => "RE: #{
# @message.subject}")
Query(Message)

# Q 125 : # Message.new(:subject => "RE: #{
# @message.subject}")
Query(Message)

# Q 126 : # Message.new
Query(Message)

# Q 127 : # @message.subject
Query(Message)
.select('subject')
# Q 128 : # User.find_active(params[:id])
Query(User)

# Q 129 : # User.find_active(params[:id])
Query(User)

# Q 130 : # User.find_active
Query(User)

# Q 131 : # self.is_default?
Query(IssueStatus)

# Q 132 : # self.created_on
Query(Token)
.select('created_on')
# Q 133 : # issue.assigned_to
Query(User)
.where("id = ?")
# Q 134 : # @user.custom_values.find(:all, :include => :custom_field)
Query(CustomValue)
.where("user_id = ?")
.where("id = ?")
# Q 135 : # @user.custom_values.find(:all, :include => :custom_field)
Query(CustomValue)
.where("user_id = ?")
.where("id = ?")
# Q 136 : # @user.custom_values.find
Query(CustomValue)
.where("user_id = ?")
.where("id = ?")
# Q 137 : # @user.custom_values
Query(CustomValue)
.where("user_id = ?")
# Q 138 : # News.with_scope(:find => @find_options)
Query(News)

# Q 139 : # News.with_scope
Query(News)

# Q 140 : # Query.new(params[:query])
Query(Query)

# Q 141 : # Query.new(params[:query])
Query(Query)

# Q 142 : # Query.new
Query(Query)

# Q 143 : # self.class.scm_name
Query(Repository)

# Q 144 : # self.class
Query(Repository)

# Q 145 : # WikiPage.new(:wiki => self, :title => Wiki.titleize(title))
Query(WikiPage)

# Q 146 : # WikiPage.new
Query(WikiPage)

# Q 147 : # Wiki.titleize(title)
Query(Wiki)

# Q 148 : # Wiki.titleize
Query(Wiki)

# Q 149 : # Setting.repositories_encodings.split(",").collect(&:strip)
Query(Setting)

# Q 150 : # Setting.repositories_encodings.split
Query(Setting)

# Q 151 : # Setting.repositories_encodings
Query(Setting)

# Q 152 : # issue.priority.name
Query(Enumeration)
.where("id = ?")
.select('name')
# Q 153 : # issue.priority
Query(Enumeration)
.where("id = ?")
# Q 154 : # Issue.table_name
Query(Issue)

# Q 155 : # News.table_name
Query(News)

# Q 156 : # News.table_name
Query(News)

# Q 157 : # News.table_name
Query(News)

# Q 158 : # @project.boards
Query(Board)
.where("project_id = ?")
# Q 159 : # @project.boards
Query(Board)
.where("project_id = ?")
# Q 160 : # @project.repository
Query(Repository)
.where("id = ?")
# Q 161 : # @project.repository
Query(Repository)
.where("id = ?")
# Q 162 : # self.user.name
Query(User)
.where("id = ?")
# Q 163 : # self.user
Query(User)
.where("id = ?")
# Q 164 : # User.find_active(:first, :conditions => { :mail => email.from.first })
Query(User)

# Q 165 : # User.find_active(:first, :conditions => { :mail => email.from.first })
Query(User)

# Q 166 : # User.find_active
Query(User)

# Q 167 : # @project.issue_categories
Query(IssueCategory)
.where("project_id = ?")
# Q 168 : # User.current.role_for_project(@project)
Query(User)

# Q 169 : # User.current.role_for_project
Query(User)

# Q 170 : # User.current
Query(User)

# Q 171 : # find(:all, :limit => count, :conditions => Project.visible_by(user), :include => [:author, :project], :order => "News.created_on DESC")
Query(News)
.where("id = ?")
# Q 172 : # Project.visible_by(user)
Query(Project)

# Q 173 : # Project.visible_by
Query(Project)

# Q 174 : # News.table_name
Query(News)

# Q 175 : # self.account
Query(AuthSourceLdap)
.select('account')
# Q 176 : # self.account_password
Query(AuthSourceLdap)
.select('account_password')
# Q 177 : # self.project
Query(Project)
.where("id = ?")
# Q 178 : # tokens.index(words.downcase)
Query(Token)

# Q 179 : # tokens.index
Query(Token)

# Q 180 : # tokens.index(words.downcase)
Query(Token)

# Q 181 : # tokens.index
Query(Token)

# Q 182 : # tokens.index(words.downcase)
Query(Token)

# Q 183 : # tokens.index
Query(Token)

# Q 184 : # @project.wiki
Query(Wiki)
.where("id = ?")
# Q 185 : # @wiki.find_or_new_page(page_title)
Query(Wiki)

# Q 186 : # @wiki.find_or_new_page(page_title)
Query(Wiki)

# Q 187 : # @wiki.find_or_new_page
Query(Wiki)

# Q 188 : # @user.memberships.select
Query(Member)
.where("user_id = ?")
# Q 189 : # @user.memberships
Query(Member)
.where("user_id = ?")
# Q 190 : # @version.destroy
Query(Version)

# Q 191 : # @boards.size
Query(Board)

# Q 192 : # User.current
Query(User)

# Q 193 : # User.current
Query(User)

# Q 194 : # Repository.factory(params[:repository_scm])
Query(Repository)

# Q 195 : # Repository.factory(params[:repository_scm])
Query(Repository)

# Q 196 : # Repository.factory
Query(Repository)

# Q 197 : # self.attr_login
Query(AuthSourceLdap)
.select('attr_login')
# Q 198 : # Issue.update_all("category_id = #{
# reassign_to.id}", "category_id = #{
# id}")
Query(Issue)

# Q 199 : # Issue.update_all
Query(Issue)

# Q 200 : # journal.journalized
Query(Journal)
.where("id = ?")
# Q 201 : # journal.journalized
Query(Journal)
.where("id = ?")
# Q 202 : # project.nil?
Query(Project)

# Q 203 : # issue.project
Query(Project)
.where("id = ?")
# Q 204 : # issue.project
Query(Project)
.where("id = ?")
# Q 205 : # journal.journalized
Query(Journal)
.where("id = ?")
# Q 206 : # journal.journalized
Query(Journal)
.where("id = ?")
# Q 207 : # issue.send(column.name)
Query(Issue)

# Q 208 : # issue.send(column.name)
Query(Issue)

# Q 209 : # issue.send
Query(Issue)

# Q 210 : # @project.wiki.destroy
Query(Wiki)
.where("id = ?")
# Q 211 : # @project.wiki
Query(Wiki)
.where("id = ?")
# Q 212 : # Comment.new(params[:comment])
Query(Comment)

# Q 213 : # Comment.new(params[:comment])
Query(Comment)

# Q 214 : # Comment.new
Query(Comment)

# Q 215 : # TimeEntry.table_name
Query(TimeEntry)

# Q 216 : # Message.new(params[:message])
Query(Message)

# Q 217 : # Message.new(params[:message])
Query(Message)

# Q 218 : # Message.new
Query(Message)

# Q 219 : # User.current.role_for_project(membership.project)
Query(User)

# Q 220 : # User.current.role_for_project
Query(User)

# Q 221 : # User.current
Query(User)

# Q 222 : # User.current.role_for_project(membership.project)
Query(User)

# Q 223 : # @member.update_attributes(params[:member])
Query(Member)

# Q 224 : # @member.update_attributes
Query(Member)

# Q 225 : # Project.find_by_identifier(identifier)
Query(Project)

# Q 226 : # Project.find_by_identifier(identifier)
Query(Project)

# Q 227 : # Project.find_by_identifier
Query(Project)

# Q 228 : # @boards.first
Query(Board)
.return_limit('1')
# Q 229 : # @boards.first
Query(Board)
.return_limit('1')
# Q 230 : # Issue.find(:first, :conditions => ["tracker_id=?", self.id])
Query(Issue)
.where("tracker_id = ?")
.where("id = ?")
.where("id = ?")
# Q 231 : # Issue.find
Query(Issue)
.where("id = ?")
# Q 232 : # self.id
Query(Tracker)

# Q 233 : # find(:first, :conditions => ["is_default=?", true])
Query(IssueStatus)
.where("is_default = ?")
.where("id = ?")
.where("id = ?")
# Q 234 : # issue.recipients
Query(Issue)

# Q 235 : # user.allowed_to?(:add_issue_notes, issue.project)
Query(User)

# Q 236 : # user.allowed_to?
Query(User)

# Q 237 : # issue.project
Query(Project)
.where("id = ?")
# Q 238 : # issue.recipients
Query(Issue)

# Q 239 : # User.current.allowed_to?(:edit_wiki_pages, @project)
Query(User)

# Q 240 : # User.current.allowed_to?
Query(User)

# Q 241 : # User.current
Query(User)

# Q 242 : # @project.users
Query(User)
.where("project_id = ?")
# Q 243 : # Issue.find_by_id($1, :include => :project, :conditions => Project.visible_by(logged_in_user))
Query(Issue)

# Q 244 : # Issue.find_by_id
Query(Issue)

# Q 245 : # Project.visible_by(logged_in_user)
Query(Project)

# Q 246 : # Project.visible_by
Query(Project)

# Q 247 : # Attachment.find(params[:id])
Query(Attachment)
.where("id = ?")
# Q 248 : # Attachment.find(params[:id])
Query(Attachment)
.where("id = ?")
# Q 249 : # Attachment.find
Query(Attachment)
.where("id = ?")
# Q 250 : # @project.versions.sort
Query(Version)
.where("project_id = ?")
# Q 251 : # @project.versions.sort
Query(Version)
.where("project_id = ?")
# Q 252 : # @project.versions
Query(Version)
.where("project_id = ?")
# Q 253 : # find(:all, :conditions => { :opt => option }, :order => "position")
Query(Enumeration)
.where("id = ?")
# Q 254 : # changesets.find_all_by_revision(revisions.collect(&:identifier), :order => "committed_on DESC")
Query(Changeset)

# Q 255 : # changesets.find_all_by_revision
Query(Changeset)

# Q 256 : # custom_field.possible_values
Query(CustomField)
.select('possible_values')
# Q 257 : # @news.comments
Query(Comment)
.where("news_id = ?")
# Q 258 : # @document.destroy
Query(Document)

# Q 259 : # Setting.check_cache
Query(Setting)

# Q 260 : # Enumeration.new(:opt => params[:opt])
Query(Enumeration)

# Q 261 : # Enumeration.new(:opt => params[:opt])
Query(Enumeration)

# Q 262 : # Enumeration.new
Query(Enumeration)

# Q 263 : # @attachment.project
Query(Attachment)

# Q 264 : # @attachment.project
Query(Attachment)

# Q 265 : # project.repository.nil?
Query(Repository)
.where("id = ?")
# Q 266 : # project.repository
Query(Repository)
.where("id = ?")
# Q 267 : # user.allowed_to?(item.url, project)
Query(User)

# Q 268 : # user.allowed_to?
Query(User)

# Q 269 : # self.base_dn
Query(AuthSourceLdap)
.select('base_dn')
# Q 270 : # self.filesize
Query(Attachment)

# Q 271 : # Setting.attachment_max_size.to_i.kilobytes
Query(Setting)

# Q 272 : # Setting.attachment_max_size.to_i
Query(Setting)

# Q 273 : # Setting.attachment_max_size
Query(Setting)

# Q 274 : # custom_field.possible_values
Query(CustomField)
.select('possible_values')
# Q 275 : # changesets.find_by_scmid(entry.lastrev.scmid)
Query(Changeset)

# Q 276 : # changesets.find_by_scmid(entry.lastrev.scmid)
Query(Changeset)

# Q 277 : # changesets.find_by_scmid
Query(Changeset)

# Q 278 : # changesets.find_by_scmid(entry.lastrev.scmid)
Query(Changeset)

# Q 279 : # changesets.find_by_scmid
Query(Changeset)

# Q 280 : # project.issue_categories
Query(IssueCategory)
.where("project_id = ?")
# Q 281 : # self.user.id
Query(User)
.where("id = ?")
# Q 282 : # self.user
Query(User)
.where("id = ?")
# Q 283 : # AuthSource.find(:all, :conditions => ["onthefly_register=?", true]).each
Query(AuthSource)
.where("onthefly_register = ?")
.where("id = ?")
.where("id = ?")
# Q 284 : # AuthSource.find(:all, :conditions => ["onthefly_register=?", true])
Query(AuthSource)
.where("onthefly_register = ?")
.where("id = ?")
.where("id = ?")
# Q 285 : # AuthSource.find
Query(AuthSource)
.where("id = ?")
# Q 286 : # Wiki.titleize(title)
Query(Wiki)

# Q 287 : # Wiki.titleize(title)
Query(Wiki)

# Q 288 : # Wiki.titleize
Query(Wiki)

# Q 289 : # issue.watcher_recipients
Query(Issue)

# Q 290 : # issue.watcher_recipients
Query(Issue)

# Q 291 : # user.name
Query(User)

# Q 292 : # IssueCustomField.new(params[:custom_field])
Query(IssueCustomField)

# Q 293 : # IssueCustomField.new(params[:custom_field])
Query(IssueCustomField)

# Q 294 : # IssueCustomField.new
Query(IssueCustomField)

# Q 295 : # IssueStatus.new
Query(IssueStatus)

# Q 296 : # IssueStatus.new
Query(IssueStatus)

# Q 297 : # Issue.table_name
Query(Issue)

# Q 298 : # Project.count(:conditions => conditions)
Query(Project)

# Q 299 : # Project.count(:conditions => conditions)
Query(Project)

# Q 300 : # Project.count
Query(Project)

# Q 301 : # @message.save
Query(Message)

# Q 302 : # Role.new(params[:role])
Query(Role)

# Q 303 : # Role.new(params[:role])
Query(Role)

# Q 304 : # Role.new
Query(Role)

# Q 305 : # project.name
Query(Project)
.select('name')
# Q 306 : # Tracker.new(params[:tracker])
Query(Tracker)

# Q 307 : # Tracker.new(params[:tracker])
Query(Tracker)

# Q 308 : # Tracker.new
Query(Tracker)

# Q 309 : # board.update_attribute(:last_message_id, self.id)
Query(Board)

# Q 310 : # board.update_attribute
Query(Board)

# Q 311 : # self.id
Query(Message)

# Q 312 : # issue.project.name
Query(Project)
.where("id = ?")
.select('name')
# Q 313 : # issue.project
Query(Project)
.where("id = ?")
# Q 314 : # issue.tracker.name
Query(Tracker)
.where("id = ?")
.select('name')
# Q 315 : # issue.tracker
Query(Tracker)
.where("id = ?")
# Q 316 : # issue.id
Query(Issue)

# Q 317 : # issue.status.name
Query(IssueStatus)
.where("id = ?")
.select('name')
# Q 318 : # issue.status
Query(IssueStatus)
.where("id = ?")
# Q 319 : # issue.subject
Query(Issue)
.select('subject')
# Q 320 : # issue.init_journal(user, email.body.chomp)
Query(Issue)

# Q 321 : # issue.init_journal
Query(Issue)

# Q 322 : # issue.project.name
Query(Project)
.where("id = ?")
.select('name')
# Q 323 : # issue.project
Query(Project)
.where("id = ?")
# Q 324 : # issue.tracker.name
Query(Tracker)
.where("id = ?")
.select('name')
# Q 325 : # issue.tracker
Query(Tracker)
.where("id = ?")
# Q 326 : # issue.id
Query(Issue)

# Q 327 : # issue.status.name
Query(IssueStatus)
.where("id = ?")
.select('name')
# Q 328 : # issue.status
Query(IssueStatus)
.where("id = ?")
# Q 329 : # issue.subject
Query(Issue)
.select('subject')
# Q 330 : # Tracker.find(params[:tracker_ids])
Query(Tracker)
.where("id = ?")
# Q 331 : # Tracker.find(params[:tracker_ids])
Query(Tracker)
.where("id = ?")
# Q 332 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 333 : # Tracker.find(:all)
Query(Tracker)
.where("id = ?")
# Q 334 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 335 : # AuthSourceLdap.new
Query(AuthSourceLdap)

# Q 336 : # AuthSourceLdap.new
Query(AuthSourceLdap)

# Q 337 : # @role.save
Query(Role)

# Q 338 : # @query.add_filter(field, params[:operators][field], params[:values][field])
Query(Query)

# Q 339 : # @query.add_filter
Query(Query)

# Q 340 : # @query.add_filter(field, params[:operators][field], params[:values][field])
Query(Query)

# Q 341 : # Repository.factory("Subversion", :project => project, :url => url)
Query(Repository)

# Q 342 : # Repository.factory("Subversion", :project => project, :url => url)
Query(Repository)

# Q 343 : # Repository.factory
Query(Repository)

# Q 344 : # @repository.save
Query(Repository)

# Q 345 : # @tracker.save
Query(Tracker)

# Q 346 : # changeset.revision
Query(Changeset)
.select('revision')
# Q 347 : # changeset.revision
Query(Changeset)
.select('revision')
# Q 348 : # changeset.revision
Query(Changeset)
.select('revision')
# Q 349 : # changes.find(:first, :conditions => ["path = ?", scm.with_leading_slash(entry.path)], :order => "Changeset.committed_on DESC")
Query(Change)
.where("path = ?")
.where("id = ?")
.where("id = ?")
# Q 350 : # changes.find(:first, :conditions => ["path = ?", scm.with_leading_slash(entry.path)], :order => "Changeset.committed_on DESC")
Query(Change)
.where("path = ?")
.where("id = ?")
.where("id = ?")
# Q 351 : # changes.find
Query(Change)
.where("id = ?")
# Q 352 : # Changeset.table_name
Query(Changeset)

# Q 353 : # changes.find(:first, :conditions => ["path = ?", scm.with_leading_slash(entry.path)], :order => "Changeset.committed_on DESC")
Query(Change)
.where("path = ?")
.where("id = ?")
.where("id = ?")
# Q 354 : # changes.find
Query(Change)
.where("id = ?")
# Q 355 : # Changeset.table_name
Query(Changeset)

# Q 356 : # Changeset.table_name
Query(Changeset)

# Q 357 : # Setting.wiki_compression
Query(Setting)

# Q 358 : # project.nil?
Query(Project)

# Q 359 : # issue.save
Query(Issue)

# Q 360 : # User.find(session[:user_id])
Query(User)
.where("id = ?")
# Q 361 : # User.find(session[:user_id])
Query(User)
.where("id = ?")
# Q 362 : # User.find
Query(User)
.where("id = ?")
# Q 363 : # @project.issue_categories.find_by_id(params[:reassign_to_id])
Query(IssueCategory)
.where("project_id = ?")
# Q 364 : # @project.issue_categories.find_by_id(params[:reassign_to_id])
Query(IssueCategory)
.where("project_id = ?")
# Q 365 : # @project.issue_categories.find_by_id
Query(IssueCategory)
.where("project_id = ?")
# Q 366 : # @project.issue_categories
Query(IssueCategory)
.where("project_id = ?")
# Q 367 : # repository.save
Query(Repository)

# Q 368 : # self.attr_firstname
Query(AuthSourceLdap)
.select('attr_firstname')
# Q 369 : # self.attr_lastname
Query(AuthSourceLdap)
.select('attr_lastname')
# Q 370 : # self.attr_mail
Query(AuthSourceLdap)
.select('attr_mail')
# Q 371 : # find(:first, :conditions => { :opt => option, :is_default => true }, :order => "position")
Query(Enumeration)
.where("id = ?")
# Q 372 : # changeset.revision
Query(Changeset)
.select('revision')
# Q 373 : # changeset.revision
Query(Changeset)
.select('revision')
# Q 374 : # changeset.revision
Query(Changeset)
.select('revision')
# Q 375 : # issue.project
Query(Project)
.where("id = ?")
# Q 376 : # @project.nil?
Query(Project)

# Q 377 : # issue.project
Query(Project)
.where("id = ?")
# Q 378 : # issue.project.name
Query(Project)
.where("id = ?")
.select('name')
# Q 379 : # issue.project
Query(Project)
.where("id = ?")
# Q 380 : # User.current.allowed_to?(tab[:action], @project)
Query(User)

# Q 381 : # User.current.allowed_to?
Query(User)

# Q 382 : # User.current
Query(User)

# Q 383 : # UserCustomField.new(params[:custom_field])
Query(UserCustomField)

# Q 384 : # UserCustomField.new(params[:custom_field])
Query(UserCustomField)

# Q 385 : # UserCustomField.new
Query(UserCustomField)

# Q 386 : # TimeEntry.table_name
Query(TimeEntry)

# Q 387 : # Setting.autologin?
Query(Setting)

# Q 388 : # Enumeration.new(params[:enumeration])
Query(Enumeration)

# Q 389 : # Enumeration.new(params[:enumeration])
Query(Enumeration)

# Q 390 : # Enumeration.new
Query(Enumeration)

# Q 391 : # Attachment.create(:container => @message, :file => file, :author => logged_in_user)
Query(Attachment)

# Q 392 : # Attachment.create
Query(Attachment)

# Q 393 : # Query.find(params[:query_id])
Query(Query)
.where("id = ?")
# Q 394 : # Query.find(params[:query_id])
Query(Query)
.where("id = ?")
# Q 395 : # Query.find
Query(Query)
.where("id = ?")
# Q 396 : # repository.id
Query(Repository)

# Q 397 : # Tracker.find_by_id(params[:copy_workflow_from])
Query(Tracker)

# Q 398 : # Tracker.find_by_id(params[:copy_workflow_from])
Query(Tracker)

# Q 399 : # Tracker.find_by_id
Query(Tracker)

# Q 400 : # @permissions.select
Query(Permission)

# Q 401 : # workflows.select { |w|
#   
#   w.role_id == role.id && w.tracker_id == tracker.id
# }.collect
Query(Workflow)

# Q 402 : # workflows.select
Query(Workflow)

# Q 403 : # role.id
Query(Role)

# Q 404 : # tracker.id
Query(Tracker)

# Q 405 : # self.id
Query(Message)

# Q 406 : # comment.strip
Query(Comment)

# Q 407 : # changeset.committed_on
Query(Changeset)
.select('committed_on')
# Q 408 : # changeset.committed_on
Query(Changeset)
.select('committed_on')
# Q 409 : # changeset.committed_on
Query(Changeset)
.select('committed_on')
# Q 410 : # change.changeset.revision
Query(Changeset)
.where("id = ?")
.select('revision')
# Q 411 : # change.changeset.revision
Query(Changeset)
.where("id = ?")
.select('revision')
# Q 412 : # change.changeset
Query(Changeset)
.where("id = ?")
# Q 413 : # change.changeset.revision
Query(Changeset)
.where("id = ?")
.select('revision')
# Q 414 : # change.changeset
Query(Changeset)
.where("id = ?")
# Q 415 : # issue.tracker.name
Query(Tracker)
.where("id = ?")
.select('name')
# Q 416 : # issue.tracker
Query(Tracker)
.where("id = ?")
# Q 417 : # issue.id
Query(Issue)

# Q 418 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 419 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 420 : # Project.find
Query(Project)
.where("id = ?")
# Q 421 : # @document.attachments.find(params[:attachment_id])
Query(Attachment)
.where("document_id = ?")
.where("id = ?")
# Q 422 : # @document.attachments.find(params[:attachment_id])
Query(Attachment)
.where("document_id = ?")
.where("id = ?")
# Q 423 : # @document.attachments.find
Query(Attachment)
.where("document_id = ?")
.where("id = ?")
# Q 424 : # @document.attachments
Query(Attachment)
.where("document_id = ?")
# Q 425 : # IssueStatus.new(params[:issue_status])
Query(IssueStatus)

# Q 426 : # IssueStatus.new(params[:issue_status])
Query(IssueStatus)

# Q 427 : # IssueStatus.new
Query(IssueStatus)

# Q 428 : # Enumeration::get_values("ACTI")
Query(Enumeration)

# Q 429 : # Enumeration::get_values
Query(Enumeration)

# Q 430 : # @enumeration.save
Query(Enumeration)

# Q 431 : # User.count(:conditions => conditions)
Query(User)

# Q 432 : # User.count(:conditions => conditions)
Query(User)

# Q 433 : # User.count
Query(User)

# Q 434 : # Enumeration::get_values("IPRI")
Query(Enumeration)

# Q 435 : # Enumeration::get_values("IPRI")
Query(Enumeration)

# Q 436 : # Enumeration::get_values
Query(Enumeration)

# Q 437 : # @query.save
Query(Query)

# Q 438 : # @version.attachments.find(params[:attachment_id])
Query(Attachment)
.where("version_id = ?")
.where("id = ?")
# Q 439 : # @version.attachments.find(params[:attachment_id])
Query(Attachment)
.where("version_id = ?")
.where("id = ?")
# Q 440 : # @version.attachments.find
Query(Attachment)
.where("version_id = ?")
.where("id = ?")
# Q 441 : # @version.attachments
Query(Attachment)
.where("version_id = ?")
# Q 442 : # Message.table_name
Query(Message)

# Q 443 : # Setting.cross_project_issue_relations?
Query(Setting)

# Q 444 : # AuthSourceLdap.get_attr(entry, self.attr_firstname)
Query(AuthSourceLdap)

# Q 445 : # AuthSourceLdap.get_attr
Query(AuthSourceLdap)

# Q 446 : # self.attr_firstname
Query(AuthSourceLdap)
.select('attr_firstname')
# Q 447 : # AuthSourceLdap.get_attr(entry, self.attr_firstname)
Query(AuthSourceLdap)

# Q 448 : # AuthSourceLdap.get_attr
Query(AuthSourceLdap)

# Q 449 : # self.attr_firstname
Query(AuthSourceLdap)
.select('attr_firstname')
# Q 450 : # changeset.committer
Query(Changeset)
.select('committer')
# Q 451 : # changeset.committer
Query(Changeset)
.select('committer')
# Q 452 : # changeset.committer
Query(Changeset)
.select('committer')
# Q 453 : # change.changeset.revision
Query(Changeset)
.where("id = ?")
.select('revision')
# Q 454 : # change.changeset.revision
Query(Changeset)
.where("id = ?")
.select('revision')
# Q 455 : # change.changeset
Query(Changeset)
.where("id = ?")
# Q 456 : # change.changeset.revision
Query(Changeset)
.where("id = ?")
.select('revision')
# Q 457 : # change.changeset
Query(Changeset)
.where("id = ?")
# Q 458 : # @attachment.increment_download
Query(Attachment)

# Q 459 : # ProjectCustomField.new(params[:custom_field])
Query(ProjectCustomField)

# Q 460 : # ProjectCustomField.new(params[:custom_field])
Query(ProjectCustomField)

# Q 461 : # ProjectCustomField.new
Query(ProjectCustomField)

# Q 462 : # @issue_status.save
Query(IssueStatus)

# Q 463 : # User.find_by_autologin_key(cookies[:autologin])
Query(User)

# Q 464 : # User.find_by_autologin_key(cookies[:autologin])
Query(User)

# Q 465 : # User.find_by_autologin_key
Query(User)

# Q 466 : # AuthSourceLdap.new(params[:auth_source])
Query(AuthSourceLdap)

# Q 467 : # AuthSourceLdap.new(params[:auth_source])
Query(AuthSourceLdap)

# Q 468 : # AuthSourceLdap.new
Query(AuthSourceLdap)

# Q 469 : # @role.setable_permissions
Query(Role)

# Q 470 : # @role.setable_permissions
Query(Role)

# Q 471 : # IssueRelation.find(params[:id])
Query(IssueRelation)
.where("id = ?")
# Q 472 : # IssueRelation.find(params[:id])
Query(IssueRelation)
.where("id = ?")
# Q 473 : # IssueRelation.find
Query(IssueRelation)
.where("id = ?")
# Q 474 : # @attachment.increment_download
Query(Attachment)

# Q 475 : # @tracker.workflows
Query(Workflow)
.where("tracker_id = ?")
# Q 476 : # AuthSourceLdap.get_attr(entry, self.attr_lastname)
Query(AuthSourceLdap)

# Q 477 : # AuthSourceLdap.get_attr
Query(AuthSourceLdap)

# Q 478 : # self.attr_lastname
Query(AuthSourceLdap)
.select('attr_lastname')
# Q 479 : # AuthSourceLdap.get_attr(entry, self.attr_lastname)
Query(AuthSourceLdap)

# Q 480 : # AuthSourceLdap.get_attr
Query(AuthSourceLdap)

# Q 481 : # self.attr_lastname
Query(AuthSourceLdap)
.select('attr_lastname')
# Q 482 : # Wiki.titleize(value)
Query(Wiki)

# Q 483 : # Wiki.titleize(value)
Query(Wiki)

# Q 484 : # Wiki.titleize
Query(Wiki)

# Q 485 : # change.changeset.committer
Query(Changeset)
.where("id = ?")
.select('committer')
# Q 486 : # change.changeset.committer
Query(Changeset)
.where("id = ?")
.select('committer')
# Q 487 : # change.changeset
Query(Changeset)
.where("id = ?")
# Q 488 : # change.changeset.committer
Query(Changeset)
.where("id = ?")
.select('committer')
# Q 489 : # change.changeset
Query(Changeset)
.where("id = ?")
# Q 490 : # changes.find_by_revision_and_path(entry.lastrev.revision, scm.with_leading_slash(entry.path))
Query(Change)
.where("revision = ?")
.where("path = ?")
# Q 491 : # changes.find_by_revision_and_path(entry.lastrev.revision, scm.with_leading_slash(entry.path))
Query(Change)
.where("revision = ?")
.where("path = ?")
# Q 492 : # changes.find_by_revision_and_path
Query(Change)
.where("revision = ?")
.where("path = ?")
# Q 493 : # changes.find_by_revision_and_path(entry.lastrev.revision, scm.with_leading_slash(entry.path))
Query(Change)
.where("revision = ?")
.where("path = ?")
# Q 494 : # changes.find_by_revision_and_path
Query(Change)
.where("revision = ?")
.where("path = ?")
# Q 495 : # changes.find_by_revision_and_path(entry.lastrev.revision, scm.with_leading_slash(entry.path))
Query(Change)
.where("revision = ?")
.where("path = ?")
# Q 496 : # changes.find_by_revision_and_path
Query(Change)
.where("revision = ?")
.where("path = ?")
# Q 497 : # repository.class.name.demodulize.underscore
Query(Repository)

# Q 498 : # repository.class.name.demodulize
Query(Repository)

# Q 499 : # repository.class.name
Query(Repository)

# Q 500 : # repository.class
Query(Repository)

# Q 501 : # IssueStatus.find_by_id(detail.value)
Query(IssueStatus)

# Q 502 : # IssueStatus.find_by_id(detail.value)
Query(IssueStatus)

# Q 503 : # IssueStatus.find_by_id
Query(IssueStatus)

# Q 504 : # @attachment.diskfile
Query(Attachment)

# Q 505 : # @attachment.filename
Query(Attachment)
.select('filename')
# Q 506 : # @project.issue_categories
Query(IssueCategory)
.where("project_id = ?")
# Q 507 : # Issue.table_name
Query(Issue)

# Q 508 : # @auth_source.save
Query(AuthSource)

# Q 509 : # @enumeration.opt
Query(Enumeration)

# Q 510 : # @member.destroy
Query(Member)

# Q 511 : # @issue.relations.include?(relation)
Query(Issue)

# Q 512 : # @issue.relations.include?
Query(Issue)

# Q 513 : # @issue.relations
Query(Issue)

# Q 514 : # query.valid?
Query(Query)

# Q 515 : # @attachment.diskfile
Query(Attachment)

# Q 516 : # @attachment.filename
Query(Attachment)
.select('filename')
# Q 517 : # AuthSourceLdap.get_attr(entry, self.attr_mail)
Query(AuthSourceLdap)

# Q 518 : # AuthSourceLdap.get_attr
Query(AuthSourceLdap)

# Q 519 : # self.attr_mail
Query(AuthSourceLdap)
.select('attr_mail')
# Q 520 : # AuthSourceLdap.get_attr(entry, self.attr_mail)
Query(AuthSourceLdap)

# Q 521 : # AuthSourceLdap.get_attr
Query(AuthSourceLdap)

# Q 522 : # self.attr_mail
Query(AuthSourceLdap)
.select('attr_mail')
# Q 523 : # self.opt
Query(Enumeration)

# Q 524 : # change.revision
Query(Change)
.select('revision')
# Q 525 : # change.revision
Query(Change)
.select('revision')
# Q 526 : # change.revision
Query(Change)
.select('revision')
# Q 527 : # repository.is_a?(Repository)
Query(Repository)

# Q 528 : # repository.is_a?
Query(Repository)

# Q 529 : # custom_value.custom_field.name
Query(CustomField)
.where("id = ?")
.select('name')
# Q 530 : # custom_value.custom_field
Query(CustomField)
.where("id = ?")
# Q 531 : # IssueStatus.find_by_id(detail.old_value)
Query(IssueStatus)

# Q 532 : # IssueStatus.find_by_id(detail.old_value)
Query(IssueStatus)

# Q 533 : # IssueStatus.find_by_id
Query(IssueStatus)

# Q 534 : # @board.topics.count
Query(Message)
.where("board_id = ?")
# Q 535 : # @board.topics.count
Query(Message)
.where("board_id = ?")
# Q 536 : # @board.topics
Query(Message)
.where("board_id = ?")
# Q 537 : # @repository.destroy
Query(Repository)

# Q 538 : # @permissions.select
Query(Permission)

# Q 539 : # self.id
Query(AuthSourceLdap)

# Q 540 : # self.id
Query(AuthSourceLdap)

# Q 541 : # self.possible_values.collect { |v|
#   
#   v unless v.empty?
# }.compact
Query(CustomField)
.select('possible_values')
.where("id != 0")
# Q 542 : # self.possible_values.collect { |v|
#   
#   v unless v.empty?
# }.compact
Query(CustomField)
.select('possible_values')
.where("id != 0")
# Q 543 : # self.possible_values.collect
Query(CustomField)
.select('possible_values')
# Q 544 : # self.possible_values
Query(CustomField)
.select('possible_values')
# Q 545 : # self.filename
Query(Attachment)
.select('filename')
# Q 546 : # change.changeset.revision
Query(Changeset)
.where("id = ?")
.select('revision')
# Q 547 : # change.changeset.revision
Query(Changeset)
.where("id = ?")
.select('revision')
# Q 548 : # change.changeset
Query(Changeset)
.where("id = ?")
# Q 549 : # change.changeset.revision
Query(Changeset)
.where("id = ?")
.select('revision')
# Q 550 : # change.changeset
Query(Changeset)
.where("id = ?")
# Q 551 : # change.changeset.revision
Query(Changeset)
.where("id = ?")
.select('revision')
# Q 552 : # change.changeset
Query(Changeset)
.where("id = ?")
# Q 553 : # document.project.recipients
Query(Project)
.where("id = ?")
# Q 554 : # document.project
Query(Project)
.where("id = ?")
# Q 555 : # document.project.recipients
Query(Project)
.where("id = ?")
# Q 556 : # document.project
Query(Project)
.where("id = ?")
# Q 557 : # custom_value.custom_field.is_required?
Query(CustomField)
.where("id = ?")
# Q 558 : # custom_value.custom_field
Query(CustomField)
.where("id = ?")
# Q 559 : # @news.comments.find(params[:comment_id]).destroy
Query(Comment)
.where("news_id = ?")
.where("id = ?")
# Q 560 : # @news.comments.find(params[:comment_id])
Query(Comment)
.where("news_id = ?")
.where("id = ?")
# Q 561 : # @news.comments.find
Query(Comment)
.where("news_id = ?")
.where("id = ?")
# Q 562 : # @news.comments
Query(Comment)
.where("news_id = ?")
# Q 563 : # User.find_by_rss_key(params[:key])
Query(User)

# Q 564 : # User.find_by_rss_key(params[:key])
Query(User)

# Q 565 : # User.find_by_rss_key
Query(User)

# Q 566 : # @issue.reload
Query(Issue)

# Q 567 : # query.valid?
Query(Query)

# Q 568 : # query.project
Query(Project)
.where("id = ?")
# Q 569 : # query.statement
Query(Query)

# Q 570 : # query.statement
Query(Query)

# Q 571 : # change.changeset.committer
Query(Changeset)
.where("id = ?")
.select('committer')
# Q 572 : # change.changeset.committer
Query(Changeset)
.where("id = ?")
.select('committer')
# Q 573 : # change.changeset
Query(Changeset)
.where("id = ?")
# Q 574 : # change.changeset.committer
Query(Changeset)
.where("id = ?")
.select('committer')
# Q 575 : # change.changeset
Query(Changeset)
.where("id = ?")
# Q 576 : # change.changeset.committer
Query(Changeset)
.where("id = ?")
.select('committer')
# Q 577 : # change.changeset
Query(Changeset)
.where("id = ?")
# Q 578 : # document.project.name
Query(Project)
.where("id = ?")
.select('name')
# Q 579 : # document.project
Query(Project)
.where("id = ?")
# Q 580 : # document.title
Query(Document)
.select('title')
# Q 581 : # document.project.name
Query(Project)
.where("id = ?")
.select('name')
# Q 582 : # document.project
Query(Project)
.where("id = ?")
# Q 583 : # document.title
Query(Document)
.select('title')
# Q 584 : # custom_value.custom_field.id
Query(CustomField)
.where("id = ?")
# Q 585 : # custom_value.custom_field
Query(CustomField)
.where("id = ?")
# Q 586 : # User.find_by_id(detail.value)
Query(User)

# Q 587 : # User.find_by_id(detail.value)
Query(User)

# Q 588 : # User.find_by_id
Query(User)

# Q 589 : # @query.valid?
Query(Query)

# Q 590 : # Role.find(params[:id])
Query(Role)
.where("id = ?")
# Q 591 : # Role.find(params[:id])
Query(Role)
.where("id = ?")
# Q 592 : # Role.find
Query(Role)
.where("id = ?")
# Q 593 : # Setting.sys_api_enabled?
Query(Setting)

# Q 594 : # @board.topics
Query(Message)
.where("board_id = ?")
# Q 595 : # self.others
Query(UserPreference)
.select('others')
# Q 596 : # change.revision
Query(Change)
.select('revision')
# Q 597 : # change.revision
Query(Change)
.select('revision')
# Q 598 : # change.revision
Query(Change)
.select('revision')
# Q 599 : # change.revision
Query(Change)
.select('revision')
# Q 600 : # role.position
Query(Role)
.select('position')
# Q 601 : # custom_value.errors.empty?
Query(CustomValue)

# Q 602 : # custom_value.errors
Query(CustomValue)

# Q 603 : # User.find_by_id(detail.old_value)
Query(User)

# Q 604 : # User.find_by_id(detail.old_value)
Query(User)

# Q 605 : # User.find_by_id
Query(User)

# Q 606 : # @custom_field.save
Query(CustomField)

# Q 607 : # User.anonymous
Query(User)

# Q 608 : # User.anonymous
Query(User)

# Q 609 : # Issue.count(:include => [:status, :project], :conditions => @query.statement)
Query(Issue)

# Q 610 : # Issue.count(:include => [:status, :project], :conditions => @query.statement)
Query(Issue)

# Q 611 : # Issue.count
Query(Issue)

# Q 612 : # @query.statement
Query(Query)

# Q 613 : # Message.new(params[:reply])
Query(Message)

# Q 614 : # Message.new(params[:reply])
Query(Message)

# Q 615 : # Message.new
Query(Message)

# Q 616 : # User.try_to_login(params[:login], params[:password])
Query(User)

# Q 617 : # User.try_to_login(params[:login], params[:password])
Query(User)

# Q 618 : # User.try_to_login
Query(User)

# Q 619 : # @project.issue_categories
Query(IssueCategory)
.where("project_id = ?")
# Q 620 : # @project.issue_categories
Query(IssueCategory)
.where("project_id = ?")
# Q 621 : # @role.update_attributes(params[:role])
Query(Role)

# Q 622 : # @role.update_attributes
Query(Role)

# Q 623 : # self.issue_from_id
Query(IssueRelation)
.select('issue_from_id')
# Q 624 : # issue.id
Query(Issue)

# Q 625 : # workflows.find(:all, :include => :new_status, :conditions => ["role_id=? and tracker_id=?", role.id, tracker.id]).collect { |w|
#   
#   w.new_status
# }.compact
Query(Workflow)
.where("id = ?")
.where("role_id = ?")
.where("tracker_id = ?")
.where("id = ?")
.where("id != 0")
# Q 626 : # workflows.find(:all, :include => :new_status, :conditions => ["role_id=? and tracker_id=?", role.id, tracker.id]).collect { |w|
#   
#   w.new_status
# }.compact
Query(Workflow)
.where("id = ?")
.where("role_id = ?")
.where("tracker_id = ?")
.where("id = ?")
.where("id != 0")
# Q 627 : # workflows.find(:all, :include => :new_status, :conditions => ["role_id=? and tracker_id=?", role.id, tracker.id]).collect
Query(Workflow)
.where("id = ?")
.where("role_id = ?")
.where("tracker_id = ?")
.where("id = ?")
# Q 628 : # workflows.find(:all, :include => :new_status, :conditions => ["role_id=? and tracker_id=?", role.id, tracker.id])
Query(Workflow)
.where("id = ?")
.where("role_id = ?")
.where("tracker_id = ?")
.where("id = ?")
# Q 629 : # workflows.find
Query(Workflow)
.where("id = ?")
# Q 630 : # board.project
Query(Project)
.where("id = ?")
# Q 631 : # Enumeration.update_all("is_default = #{
# connection.quoted_false}", { :opt => opt })
Query(Enumeration)

# Q 632 : # Enumeration.update_all
Query(Enumeration)

# Q 633 : # change.branch
Query(Change)
.select('branch')
# Q 634 : # change.branch
Query(Change)
.select('branch')
# Q 635 : # change.branch
Query(Change)
.select('branch')
# Q 636 : # change.branch
Query(Change)
.select('branch')
# Q 637 : # IssueCategory.find(params[:id])
Query(IssueCategory)
.where("id = ?")
# Q 638 : # IssueCategory.find(params[:id])
Query(IssueCategory)
.where("id = ?")
# Q 639 : # IssueCategory.find
Query(IssueCategory)
.where("id = ?")
# Q 640 : # User.current.allowed_to?("view_#{
# o}".to_sym, @project)
Query(User)

# Q 641 : # User.current.allowed_to?
Query(User)

# Q 642 : # User.current
Query(User)

# Q 643 : # Issue.with_scope(:find => @find_options)
Query(Issue)

# Q 644 : # Issue.with_scope
Query(Issue)

# Q 645 : # @permissions.select
Query(Permission)

# Q 646 : # self.field_format
Query(CustomField)
.select('field_format')
# Q 647 : # Wiki.titleize(title)
Query(Wiki)

# Q 648 : # Wiki.titleize(title)
Query(Wiki)

# Q 649 : # Wiki.titleize
Query(Wiki)

# Q 650 : # Issue.count(:all, :conditions => ["fixed_version_id = ? AND is_closed = ?", self.id, false], :include => :status)
Query(Issue)

# Q 651 : # Issue.count
Query(Issue)

# Q 652 : # self.id
Query(Version)

# Q 653 : # Change.find(:all, :include => :changeset, :conditions => ["repository_id = ? AND path = ?", id, path], :order => "committed_on DESC, Changeset.revision DESC").collect(&:changeset)
Query(Change)
.where("id = ?")
.where("repository_id = ?")
.where("path = ?")
.where("id = ?")
# Q 654 : # Change.find(:all, :include => :changeset, :conditions => ["repository_id = ? AND path = ?", id, path], :order => "committed_on DESC, Changeset.revision DESC").collect
Query(Change)
.where("id = ?")
.where("repository_id = ?")
.where("path = ?")
.where("id = ?")
# Q 655 : # Change.find(:all, :include => :changeset, :conditions => ["repository_id = ? AND path = ?", id, path], :order => "committed_on DESC, Changeset.revision DESC")
Query(Change)
.where("id = ?")
.where("repository_id = ?")
.where("path = ?")
.where("id = ?")
# Q 656 : # Change.find
Query(Change)
.where("id = ?")
# Q 657 : # Enumeration.find_by_id(detail.value)
Query(Enumeration)

# Q 658 : # Enumeration.find_by_id(detail.value)
Query(Enumeration)

# Q 659 : # Enumeration.find_by_id
Query(Enumeration)

# Q 660 : # @custom_field.type
Query(CustomField)
.select('type')
# Q 661 : # @user.pref
Query(User)

# Q 662 : # @version.attachments.find(params[:attachment_id]).destroy
Query(Attachment)
.where("version_id = ?")
.where("id = ?")
# Q 663 : # @version.attachments.find(params[:attachment_id])
Query(Attachment)
.where("version_id = ?")
.where("id = ?")
# Q 664 : # @version.attachments.find
Query(Attachment)
.where("version_id = ?")
.where("id = ?")
# Q 665 : # @version.attachments
Query(Attachment)
.where("version_id = ?")
# Q 666 : # role.id
Query(Role)

# Q 667 : # tracker.id
Query(Tracker)

# Q 668 : # self.possible_values.nil?
Query(CustomField)
.select('possible_values')
# Q 669 : # self.possible_values
Query(CustomField)
.select('possible_values')
# Q 670 : # self.possible_values.empty?
Query(CustomField)
.select('possible_values')
# Q 671 : # self.possible_values
Query(CustomField)
.select('possible_values')
# Q 672 : # changesets.find_by_revision(rev)
Query(Changeset)

# Q 673 : # changesets.find_by_revision(rev)
Query(Changeset)

# Q 674 : # changesets.find_by_revision
Query(Changeset)

# Q 675 : # Enumeration.find_by_id(detail.old_value)
Query(Enumeration)

# Q 676 : # Enumeration.find_by_id(detail.old_value)
Query(Enumeration)

# Q 677 : # Enumeration.find_by_id
Query(Enumeration)

# Q 678 : # @news.destroy
Query(News)

# Q 679 : # Enumeration.find(params[:id])
Query(Enumeration)
.where("id = ?")
# Q 680 : # Enumeration.find(params[:id])
Query(Enumeration)
.where("id = ?")
# Q 681 : # Enumeration.find
Query(Enumeration)
.where("id = ?")
# Q 682 : # @message.children
Query(Message)

# Q 683 : # Issue.table_name
Query(Issue)

# Q 684 : # Issue.table_name
Query(Issue)

# Q 685 : # Issue.table_name
Query(Issue)

# Q 686 : # Setting.autofetch_changesets?
Query(Setting)

# Q 687 : # @repository.fetch_changesets
Query(Repository)

# Q 688 : # self.possible_values
Query(CustomField)
.select('possible_values')
# Q 689 : # changesets.find_by_revision(rev_to)
Query(Changeset)

# Q 690 : # changesets.find_by_revision(rev_to)
Query(Changeset)

# Q 691 : # changesets.find_by_revision
Query(Changeset)

# Q 692 : # Changeset.table_name
Query(Changeset)

# Q 693 : # repository.class.name.demodulize
Query(Repository)

# Q 694 : # repository.class.name
Query(Repository)

# Q 695 : # repository.class
Query(Repository)

# Q 696 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 697 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 698 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 699 : # IssueStatus.find(params[:id])
Query(IssueStatus)
.where("id = ?")
# Q 700 : # IssueStatus.find(params[:id])
Query(IssueStatus)
.where("id = ?")
# Q 701 : # IssueStatus.find
Query(IssueStatus)
.where("id = ?")
# Q 702 : # @query.statement
Query(Query)

# Q 703 : # Setting.autologin?
Query(Setting)

# Q 704 : # @role.setable_permissions
Query(Role)

# Q 705 : # @role.setable_permissions
Query(Role)

# Q 706 : # self.issue_from_id
Query(IssueRelation)
.select('issue_from_id')
# Q 707 : # issue.id
Query(Issue)

# Q 708 : # enumeration.position
Query(Enumeration)
.select('position')
# Q 709 : # self.builtin
Query(Role)
.select('builtin')
# Q 710 : # attachments.first.container
Query(Attachment)
.return_limit('1')
.where("id = ?")
# Q 711 : # attachments.first.container
Query(Attachment)
.return_limit('1')
.where("id = ?")
# Q 712 : # attachments.first
Query(Attachment)
.return_limit('1')
# Q 713 : # attachments.first.container
Query(Attachment)
.return_limit('1')
.where("id = ?")
# Q 714 : # attachments.first.container
Query(Attachment)
.return_limit('1')
.where("id = ?")
# Q 715 : # attachments.first
Query(Attachment)
.return_limit('1')
# Q 716 : # repository.new_record?
Query(Repository)

# Q 717 : # IssueCategory.find_by_id(detail.value)
Query(IssueCategory)

# Q 718 : # IssueCategory.find_by_id(detail.value)
Query(IssueCategory)

# Q 719 : # IssueCategory.find_by_id
Query(IssueCategory)

# Q 720 : # AuthSource.find(params[:id])
Query(AuthSource)
.where("id = ?")
# Q 721 : # AuthSource.find(params[:id])
Query(AuthSource)
.where("id = ?")
# Q 722 : # AuthSource.find
Query(AuthSource)
.where("id = ?")
# Q 723 : # Token.create(:user => user, :action => "autologin")
Query(Token)

# Q 724 : # Token.create(:user => user, :action => "autologin")
Query(Token)

# Q 725 : # Token.create
Query(Token)

# Q 726 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 727 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 728 : # Project.find
Query(Project)
.where("id = ?")
# Q 729 : # @project.name
Query(Project)
.select('name')
# Q 730 : # Setting.app_title
Query(Setting)

# Q 731 : # query.name
Query(Query)
.select('name')
# Q 732 : # @repository.entries("")
Query(Repository)

# Q 733 : # @repository.entries("")
Query(Repository)

# Q 734 : # @repository.entries
Query(Repository)

# Q 735 : # Tracker.find(params[:id])
Query(Tracker)
.where("id = ?")
# Q 736 : # Tracker.find(params[:id])
Query(Tracker)
.where("id = ?")
# Q 737 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 738 : # @permissions.collect(&:project_module).uniq
Query(Permission)
.distinct('')
# Q 739 : # IssueStatus.default
Query(IssueStatus)

# Q 740 : # wiki.redirects.find_all_by_redirects_to(@previous_title).each
Query(Wiki)

# Q 741 : # wiki.redirects.find_all_by_redirects_to(@previous_title)
Query(Wiki)

# Q 742 : # wiki.redirects.find_all_by_redirects_to
Query(Wiki)

# Q 743 : # wiki.redirects
Query(Wiki)

# Q 744 : # Issue.count(:all, :conditions => ["fixed_version_id = ? AND is_closed = ?", self.id, true], :include => :status)
Query(Issue)

# Q 745 : # Issue.count
Query(Issue)

# Q 746 : # self.id
Query(Version)

# Q 747 : # change.path
Query(Change)
.select('path')
# Q 748 : # IssueCategory.find_by_id(detail.old_value)
Query(IssueCategory)

# Q 749 : # IssueCategory.find_by_id(detail.old_value)
Query(IssueCategory)

# Q 750 : # IssueCategory.find_by_id
Query(IssueCategory)

# Q 751 : # Attachment.create(:container => @document, :file => file, :author => logged_in_user)
Query(Attachment)

# Q 752 : # Attachment.create(:container => @document, :file => file, :author => logged_in_user)
Query(Attachment)

# Q 753 : # Attachment.create
Query(Attachment)

# Q 754 : # token.value
Query(Token)
.select('value')
# Q 755 : # @project.members.collect
Query(Member)
.where("project_id = ?")
# Q 756 : # @project.members
Query(Member)
.where("project_id = ?")
# Q 757 : # @query.add_filter(field, params[:operators][field], params[:values][field])
Query(Query)

# Q 758 : # @query.add_filter
Query(Query)

# Q 759 : # @query.add_filter(field, params[:operators][field], params[:values][field])
Query(Query)

# Q 760 : # @tracker.update_attributes(params[:tracker])
Query(Tracker)

# Q 761 : # @tracker.update_attributes
Query(Tracker)

# Q 762 : # Enumeration.default("IPRI")
Query(Enumeration)

# Q 763 : # Enumeration.default
Query(Enumeration)

# Q 764 : # comments.blank?
Query(Comment)

# Q 765 : # User.current.logged?
Query(User)

# Q 766 : # User.current
Query(User)

# Q 767 : # User.current
Query(User)

# Q 768 : # User.current
Query(User)

# Q 769 : # Enumeration.find(params[:id])
Query(Enumeration)
.where("id = ?")
# Q 770 : # Enumeration.find(params[:id])
Query(Enumeration)
.where("id = ?")
# Q 771 : # Enumeration.find
Query(Enumeration)
.where("id = ?")
# Q 772 : # Project.visible_by(logged_in_user)
Query(Project)

# Q 773 : # Project.visible_by
Query(Project)

# Q 774 : # @repository.changesets.find(:all, :limit => 10, :order => "committed_on DESC")
Query(Changeset)
.where("repository_id = ?")
.where("id = ?")
# Q 775 : # @repository.changesets.find(:all, :limit => 10, :order => "committed_on DESC")
Query(Changeset)
.where("repository_id = ?")
.where("id = ?")
# Q 776 : # @repository.changesets.find
Query(Changeset)
.where("repository_id = ?")
.where("id = ?")
# Q 777 : # @repository.changesets
Query(Changeset)
.where("repository_id = ?")
# Q 778 : # Changeset.create(:repository => self, :revision => revision.identifier, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 779 : # Changeset.create(:repository => self, :revision => revision.identifier, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 780 : # Changeset.create
Query(Changeset)

# Q 781 : # Changeset.create(:repository => self, :revision => revision.identifier, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 782 : # Changeset.create
Query(Changeset)

# Q 783 : # Changeset.create(:repository => self, :revision => revision.identifier, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 784 : # Changeset.create
Query(Changeset)

# Q 785 : # changesets.find(:first)
Query(Changeset)
.where("id = ?")
# Q 786 : # changesets.find
Query(Changeset)
.where("id = ?")
# Q 787 : # Version.find_by_id(detail.value)
Query(Version)

# Q 788 : # Version.find_by_id(detail.value)
Query(Version)

# Q 789 : # Version.find_by_id
Query(Version)

# Q 790 : # CustomField.find(params[:id])
Query(CustomField)
.where("id = ?")
# Q 791 : # CustomField.find(params[:id])
Query(CustomField)
.where("id = ?")
# Q 792 : # CustomField.find
Query(CustomField)
.where("id = ?")
# Q 793 : # IssueStatus.find(params[:id])
Query(IssueStatus)
.where("id = ?")
# Q 794 : # IssueStatus.find(params[:id])
Query(IssueStatus)
.where("id = ?")
# Q 795 : # IssueStatus.find
Query(IssueStatus)
.where("id = ?")
# Q 796 : # Setting.login_required?
Query(Setting)

# Q 797 : # @user.pref
Query(User)

# Q 798 : # @user.pref
Query(User)

# Q 799 : # @enumeration.update_attributes(params[:enumeration])
Query(Enumeration)

# Q 800 : # @enumeration.update_attributes
Query(Enumeration)

# Q 801 : # User.new(:language => Setting.default_language)
Query(User)

# Q 802 : # User.new(:language => Setting.default_language)
Query(User)

# Q 803 : # User.new
Query(User)

# Q 804 : # Setting.default_language
Query(Setting)

# Q 805 : # Role.find(params[:id])
Query(Role)
.where("id = ?")
# Q 806 : # Role.find(params[:id])
Query(Role)
.where("id = ?")
# Q 807 : # Role.find
Query(Role)
.where("id = ?")
# Q 808 : # Issue.find(params[:issue_id])
Query(Issue)
.where("id = ?")
# Q 809 : # Issue.find(params[:issue_id])
Query(Issue)
.where("id = ?")
# Q 810 : # Issue.find
Query(Issue)
.where("id = ?")
# Q 811 : # @changesets.any?
Query(Changeset)

# Q 812 : # workflows.find(:first, :conditions => { :new_status_id => status.id, :role_id => role.id, :tracker_id => tracker.id }).nil?
Query(Workflow)
.where("id = ?")
# Q 813 : # workflows.find(:first, :conditions => { :new_status_id => status.id, :role_id => role.id, :tracker_id => tracker.id })
Query(Workflow)
.where("id = ?")
# Q 814 : # workflows.find
Query(Workflow)
.where("id = ?")
# Q 815 : # role.id
Query(Role)

# Q 816 : # tracker.id
Query(Tracker)

# Q 817 : # Setting.commit_ref_keywords.downcase.split(",").collect(&:strip)
Query(Setting)

# Q 818 : # Setting.commit_ref_keywords.downcase.split(",").collect(&:strip)
Query(Setting)

# Q 819 : # Setting.commit_ref_keywords.downcase.split
Query(Setting)

# Q 820 : # Setting.commit_ref_keywords.downcase
Query(Setting)

# Q 821 : # Setting.commit_ref_keywords
Query(Setting)

# Q 822 : # Version.find_by_id(detail.old_value)
Query(Version)

# Q 823 : # Version.find_by_id(detail.old_value)
Query(Version)

# Q 824 : # Version.find_by_id
Query(Version)

# Q 825 : # News.find(params[:id])
Query(News)
.where("id = ?")
# Q 826 : # News.find(params[:id])
Query(News)
.where("id = ?")
# Q 827 : # News.find
Query(News)
.where("id = ?")
# Q 828 : # @attachments.empty?
Query(Attachment)

# Q 829 : # Setting.notified_events.include?("document_added")
Query(Setting)

# Q 830 : # Setting.notified_events.include?
Query(Setting)

# Q 831 : # Setting.notified_events
Query(Setting)

# Q 832 : # @custom_field.update_attributes(params[:custom_field])
Query(CustomField)

# Q 833 : # @custom_field.update_attributes
Query(CustomField)

# Q 834 : # @issue_status.update_attributes(params[:issue_status])
Query(IssueStatus)

# Q 835 : # @issue_status.update_attributes
Query(IssueStatus)

# Q 836 : # AuthSource.find(params[:id])
Query(AuthSource)
.where("id = ?")
# Q 837 : # AuthSource.find(params[:id])
Query(AuthSource)
.where("id = ?")
# Q 838 : # AuthSource.find
Query(AuthSource)
.where("id = ?")
# Q 839 : # Board.find(params[:board_id], :include => :project)
Query(Board)
.where("id = ?")
# Q 840 : # Board.find(params[:board_id], :include => :project)
Query(Board)
.where("id = ?")
# Q 841 : # Board.find
Query(Board)
.where("id = ?")
# Q 842 : # UserCustomField.find(:all).collect
Query(UserCustomField)
.where("id = ?")
# Q 843 : # UserCustomField.find(:all)
Query(UserCustomField)
.where("id = ?")
# Q 844 : # UserCustomField.find
Query(UserCustomField)
.where("id = ?")
# Q 845 : # CustomValue.new(:custom_field => x, :customized => @user)
Query(CustomValue)

# Q 846 : # CustomValue.new
Query(CustomValue)

# Q 847 : # @issue.project
Query(Project)
.where("id = ?")
# Q 848 : # @issue.project
Query(Project)
.where("id = ?")
# Q 849 : # Version.find(params[:id])
Query(Version)
.where("id = ?")
# Q 850 : # Version.find(params[:id])
Query(Version)
.where("id = ?")
# Q 851 : # Version.find
Query(Version)
.where("id = ?")
# Q 852 : # projects.group_by
Query(Project)

# Q 853 : # Board.new(params[:board])
Query(Board)

# Q 854 : # Board.new(params[:board])
Query(Board)

# Q 855 : # Board.new
Query(Board)

# Q 856 : # @permissions.select
Query(Permission)

# Q 857 : # find(:all, :conditions => ["is_for_all=?", true])
Query(CustomField)
.where("is_for_all = ?")
.where("id = ?")
.where("id = ?")
# Q 858 : # project.wiki
Query(Wiki)
.where("id = ?")
# Q 859 : # self.builtin?
Query(Role)

# Q 860 : # @wiki.find_or_new_page(params[:page])
Query(Wiki)

# Q 861 : # @wiki.find_or_new_page(params[:page])
Query(Wiki)

# Q 862 : # @wiki.find_or_new_page
Query(Wiki)

# Q 863 : # @news.project
Query(Project)
.where("id = ?")
# Q 864 : # @news.project
Query(Project)
.where("id = ?")
# Q 865 : # @auth_source.update_attributes(params[:auth_source])
Query(AuthSource)

# Q 866 : # @auth_source.update_attributes
Query(AuthSource)

# Q 867 : # @enumeration.opt
Query(Enumeration)

# Q 868 : # @board.project
Query(Project)
.where("id = ?")
# Q 869 : # @board.project
Query(Project)
.where("id = ?")
# Q 870 : # @version.project
Query(Project)
.where("id = ?")
# Q 871 : # @version.project
Query(Project)
.where("id = ?")
# Q 872 : # setting.save
Query(Setting)

# Q 873 : # wiki.redirects.find_all_by_title(title).each(&:destroy)
Query(Wiki)

# Q 874 : # wiki.redirects.find_all_by_title(title).each
Query(Wiki)

# Q 875 : # wiki.redirects.find_all_by_title(title)
Query(Wiki)

# Q 876 : # wiki.redirects.find_all_by_title
Query(Wiki)

# Q 877 : # wiki.redirects
Query(Wiki)

# Q 878 : # Setting.commit_fix_keywords.downcase.split(",").collect(&:strip)
Query(Setting)

# Q 879 : # Setting.commit_fix_keywords.downcase.split(",").collect(&:strip)
Query(Setting)

# Q 880 : # Setting.commit_fix_keywords.downcase.split
Query(Setting)

# Q 881 : # Setting.commit_fix_keywords.downcase
Query(Setting)

# Q 882 : # Setting.commit_fix_keywords
Query(Setting)

# Q 883 : # project.wiki.find_page(wiki_page_title)
Query(Wiki)
.where("id = ?")
# Q 884 : # project.wiki.find_page
Query(Wiki)
.where("id = ?")
# Q 885 : # project.wiki
Query(Wiki)
.where("id = ?")
# Q 886 : # custom_value.value
Query(CustomValue)
.select('value')
# Q 887 : # custom_value.custom_field.field_format
Query(CustomField)
.where("id = ?")
.select('field_format')
# Q 888 : # custom_value.custom_field
Query(CustomField)
.where("id = ?")
# Q 889 : # WikiContent.new(:page => @page)
Query(WikiContent)

# Q 890 : # WikiContent.new(:page => @page)
Query(WikiContent)

# Q 891 : # WikiContent.new
Query(WikiContent)

# Q 892 : # Tracker.find(params[:tracker_ids])
Query(Tracker)
.where("id = ?")
# Q 893 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 894 : # @board.topics.find(params[:id])
Query(Message)
.where("board_id = ?")
.where("id = ?")
# Q 895 : # @board.topics.find(params[:id])
Query(Message)
.where("board_id = ?")
.where("id = ?")
# Q 896 : # @board.topics.find
Query(Message)
.where("board_id = ?")
.where("id = ?")
# Q 897 : # @board.topics
Query(Message)
.where("board_id = ?")
# Q 898 : # User.new(params[:user])
Query(User)

# Q 899 : # User.new(params[:user])
Query(User)

# Q 900 : # User.new
Query(User)

# Q 901 : # Member.find(params[:id])
Query(Member)
.where("id = ?")
# Q 902 : # Member.find(params[:id])
Query(Member)
.where("id = ?")
# Q 903 : # Member.find
Query(Member)
.where("id = ?")
# Q 904 : # @board.save
Query(Board)

# Q 905 : # setting.value
Query(Setting)
.select('value')
# Q 906 : # Issue.find(arg)
Query(Issue)
.where("id = ?")
# Q 907 : # Issue.find
Query(Issue)
.where("id = ?")
# Q 908 : # self.diskfile
Query(Attachment)

# Q 909 : # self.opt
Query(Enumeration)

# Q 910 : # changesets.find_by_revision(scm_revision)
Query(Changeset)

# Q 911 : # changesets.find_by_revision
Query(Changeset)

# Q 912 : # changesets.find_by_revision(rev)
Query(Changeset)

# Q 913 : # changesets.find_by_revision(rev)
Query(Changeset)

# Q 914 : # changesets.find_by_revision
Query(Changeset)

# Q 915 : # self.changesets.each(&:scan_comment_for_issue_ids)
Query(Changeset)
.where("repository_id = ?")
# Q 916 : # self.changesets.each
Query(Changeset)
.where("repository_id = ?")
# Q 917 : # self.changesets
Query(Changeset)
.where("repository_id = ?")
# Q 918 : # CustomField.find_by_id(detail.prop_key)
Query(CustomField)

# Q 919 : # CustomField.find_by_id(detail.prop_key)
Query(CustomField)

# Q 920 : # CustomField.find_by_id
Query(CustomField)

# Q 921 : # @user.pref
Query(User)

# Q 922 : # @tokens.empty?
Query(Token)

# Q 923 : # @project.active_children
Query(Project)

# Q 924 : # @project.active_children
Query(Project)

# Q 925 : # @role.destroy
Query(Role)

# Q 926 : # @member.project
Query(Project)
.where("id = ?")
# Q 927 : # @member.project
Query(Project)
.where("id = ?")
# Q 928 : # @query.save
Query(Query)

# Q 929 : # @repository.entries(@path, @rev)
Query(Repository)

# Q 930 : # @repository.entries(@path, @rev)
Query(Repository)

# Q 931 : # @repository.entries
Query(Repository)

# Q 932 : # issue.attributes.dup
Query(Issue)

# Q 933 : # issue.attributes.dup
Query(Issue)

# Q 934 : # issue.attributes
Query(Issue)

# Q 935 : # wiki.redirects
Query(Wiki)

# Q 936 : # IssueStatus.find_by_id(Setting.commit_fix_status_id)
Query(IssueStatus)

# Q 937 : # IssueStatus.find_by_id(Setting.commit_fix_status_id)
Query(IssueStatus)

# Q 938 : # IssueStatus.find_by_id
Query(IssueStatus)

# Q 939 : # Setting.commit_fix_status_id
Query(Setting)

# Q 940 : # User.current.language.blank?
Query(User)
.select('language')
# Q 941 : # User.current.language
Query(User)
.select('language')
# Q 942 : # User.current
Query(User)

# Q 943 : # User.current.language.to_sym
Query(User)
.select('language')
# Q 944 : # User.current.language
Query(User)
.select('language')
# Q 945 : # User.current
Query(User)

# Q 946 : # @user.save
Query(User)

# Q 947 : # Query.find(params[:query_id])
Query(Query)
.where("id = ?")
# Q 948 : # Query.find(params[:query_id])
Query(Query)
.where("id = ?")
# Q 949 : # Query.find
Query(Query)
.where("id = ?")
# Q 950 : # Tracker.find(params[:id])
Query(Tracker)
.where("id = ?")
# Q 951 : # Tracker.find(params[:id])
Query(Tracker)
.where("id = ?")
# Q 952 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 953 : # self.account
Query(AuthSourceLdap)
.select('account')
# Q 954 : # self.account_password
Query(AuthSourceLdap)
.select('account_password')
# Q 955 : # issue.custom_values.collect
Query(CustomValue)
.where("issue_id = ?")
# Q 956 : # issue.custom_values
Query(CustomValue)
.where("issue_id = ?")
# Q 957 : # Setting.commit_fix_done_ratio.blank?
Query(Setting)

# Q 958 : # Setting.commit_fix_done_ratio
Query(Setting)

# Q 959 : # Setting.commit_fix_done_ratio.to_i
Query(Setting)

# Q 960 : # Setting.commit_fix_done_ratio
Query(Setting)

# Q 961 : # self.password
Query(User)

# Q 962 : # User.hash_password(self.password)
Query(User)

# Q 963 : # User.hash_password(self.password)
Query(User)

# Q 964 : # User.hash_password
Query(User)

# Q 965 : # self.password
Query(User)

# Q 966 : # Issue.find(:first, :conditions => ["priority_id=?", self.id])
Query(Issue)
.where("priority_id = ?")
.where("id = ?")
.where("id = ?")
# Q 967 : # Issue.find
Query(Issue)
.where("id = ?")
# Q 968 : # self.id
Query(Enumeration)

# Q 969 : # changesets.find_by_revision(rev_to)
Query(Changeset)

# Q 970 : # changesets.find_by_revision(rev_to)
Query(Changeset)

# Q 971 : # changesets.find_by_revision
Query(Changeset)

# Q 972 : # custom_field.name
Query(CustomField)
.select('name')
# Q 973 : # custom_field.name
Query(CustomField)
.select('name')
# Q 974 : # @document.attachments.find(params[:attachment_id]).destroy
Query(Attachment)
.where("document_id = ?")
.where("id = ?")
# Q 975 : # @document.attachments.find(params[:attachment_id])
Query(Attachment)
.where("document_id = ?")
.where("id = ?")
# Q 976 : # @document.attachments.find
Query(Attachment)
.where("document_id = ?")
.where("id = ?")
# Q 977 : # @document.attachments
Query(Attachment)
.where("document_id = ?")
# Q 978 : # @custom_field.type
Query(CustomField)
.select('type')
# Q 979 : # User.current.language
Query(User)
.select('language')
# Q 980 : # User.current
Query(User)

# Q 981 : # @user.pref.save
Query(User)

# Q 982 : # @user.pref
Query(User)

# Q 983 : # @tokens.size
Query(Token)

# Q 984 : # @user.auth_source_id
Query(User)
.select('auth_source_id')
# Q 985 : # Change.create(:changeset => changeset, :action => change[:action], :path => change[:path], :from_path => change[:from_path], :from_revision => change[:from_revision])
Query(Change)

# Q 986 : # Change.create
Query(Change)

# Q 987 : # Change.create(:changeset => changeset, :action => change[:action], :path => change[:path], :from_path => change[:from_path], :from_revision => change[:from_revision])
Query(Change)

# Q 988 : # Change.create(:changeset => changeset, :action => change[:action], :path => change[:path], :from_path => change[:from_path], :from_revision => change[:from_revision])
Query(Change)

# Q 989 : # Change.create(:changeset => changeset, :action => change[:action], :path => change[:path], :from_path => change[:from_path], :from_revision => change[:from_revision])
Query(Change)

# Q 990 : # custom_field.field_format
Query(CustomField)
.select('field_format')
# Q 991 : # @issue.custom_values.find(:all, :include => :custom_field)
Query(CustomValue)
.where("issue_id = ?")
.where("id = ?")
# Q 992 : # @issue.custom_values.find(:all, :include => :custom_field)
Query(CustomValue)
.where("issue_id = ?")
.where("id = ?")
# Q 993 : # @issue.custom_values.find
Query(CustomValue)
.where("issue_id = ?")
.where("id = ?")
# Q 994 : # @issue.custom_values
Query(CustomValue)
.where("issue_id = ?")
# Q 995 : # UserCustomField.find(:all).collect
Query(UserCustomField)
.where("id = ?")
# Q 996 : # UserCustomField.find(:all)
Query(UserCustomField)
.where("id = ?")
# Q 997 : # UserCustomField.find
Query(UserCustomField)
.where("id = ?")
# Q 998 : # CustomValue.new(:custom_field => x, :customized => @user, :value => (
# params[:custom_fields] ? params["custom_fields"][x.id.to_s] : nil))
Query(CustomValue)

# Q 999 : # CustomValue.new
Query(CustomValue)

# Q 1000 : # IssueCustomField.find(:all)
Query(IssueCustomField)
.where("id = ?")
# Q 1001 : # IssueCustomField.find(:all)
Query(IssueCustomField)
.where("id = ?")
# Q 1002 : # IssueCustomField.find
Query(IssueCustomField)
.where("id = ?")
# Q 1003 : # Document.find(:first, :conditions => ["category_id=?", self.id])
Query(Document)
.where("category_id = ?")
.where("id = ?")
.where("id = ?")
# Q 1004 : # Document.find
Query(Document)
.where("id = ?")
# Q 1005 : # self.id
Query(Enumeration)

# Q 1006 : # Changeset.create(:repository => self, :revision => revision.identifier, :scmid => revision.scmid, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1007 : # Changeset.create(:repository => self, :revision => revision.identifier, :scmid => revision.scmid, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1008 : # Changeset.create
Query(Changeset)

# Q 1009 : # Changeset.create(:repository => self, :revision => revision.identifier, :scmid => revision.scmid, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1010 : # Changeset.create
Query(Changeset)

# Q 1011 : # Changeset.create(:repository => self, :revision => revision.identifier, :scmid => revision.scmid, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1012 : # Changeset.create
Query(Changeset)

# Q 1013 : # repository.root_url.blank?
Query(Repository)
.select('root_url')
# Q 1014 : # repository.root_url
Query(Repository)
.select('root_url')
# Q 1015 : # custom_field.field_format
Query(CustomField)
.select('field_format')
# Q 1016 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 1017 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 1018 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 1019 : # @issue.journals.find(:all, :include => [:user, :details], :order => "Journal.created_on ASC")
Query(Journal)
.where("issue_id = ?")
.where("id = ?")
# Q 1020 : # @issue.journals.find(:all, :include => [:user, :details], :order => "Journal.created_on ASC")
Query(Journal)
.where("issue_id = ?")
.where("id = ?")
# Q 1021 : # @issue.journals.find
Query(Journal)
.where("issue_id = ?")
.where("id = ?")
# Q 1022 : # @issue.journals
Query(Journal)
.where("issue_id = ?")
# Q 1023 : # Journal.table_name
Query(Journal)

# Q 1024 : # @user.language
Query(User)
.select('language')
# Q 1025 : # @tokens.collect
Query(Token)

# Q 1026 : # query.valid?
Query(Query)

# Q 1027 : # Project.find(:all, :conditions => "parent_id IS NULL AND status = #{
# Project::STATUS_ACTIVE}")
Query(Project)
.where("id = ?")
# Q 1028 : # Project.find(:all, :conditions => "parent_id IS NULL AND status = #{
# Project::STATUS_ACTIVE}")
Query(Project)
.where("id = ?")
# Q 1029 : # Project.find
Query(Project)
.where("id = ?")
# Q 1030 : # @tracker.move_to_top
Query(Tracker)

# Q 1031 : # Issue.find(:first, :conditions => ["status_id=?", self.id])
Query(Issue)
.where("status_id = ?")
.where("id = ?")
.where("id = ?")
# Q 1032 : # Issue.find
Query(Issue)
.where("id = ?")
# Q 1033 : # self.id
Query(IssueStatus)

# Q 1034 : # User.current
Query(User)

# Q 1035 : # Enumeration.find(params[:id])
Query(Enumeration)
.where("id = ?")
# Q 1036 : # Enumeration.find(params[:id])
Query(Enumeration)
.where("id = ?")
# Q 1037 : # Enumeration.find
Query(Enumeration)
.where("id = ?")
# Q 1038 : # @user.save
Query(User)

# Q 1039 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 1040 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 1041 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 1042 : # Project.new(params[:project])
Query(Project)

# Q 1043 : # Project.new(params[:project])
Query(Project)

# Q 1044 : # Project.new
Query(Project)

# Q 1045 : # self.successor_soonest_start
Query(IssueRelation)

# Q 1046 : # self.successor_soonest_start
Query(IssueRelation)

# Q 1047 : # TimeEntry.find(:first, :conditions => ["activity_id=?", self.id])
Query(TimeEntry)
.where("activity_id = ?")
.where("id = ?")
.where("id = ?")
# Q 1048 : # TimeEntry.find
Query(TimeEntry)
.where("id = ?")
# Q 1049 : # self.id
Query(Enumeration)

# Q 1050 : # changesets.find_by_scmid(scm_revision)
Query(Changeset)

# Q 1051 : # changesets.find_by_scmid
Query(Changeset)

# Q 1052 : # IssueStatus.find(params[:id])
Query(IssueStatus)
.where("id = ?")
# Q 1053 : # IssueStatus.find(params[:id])
Query(IssueStatus)
.where("id = ?")
# Q 1054 : # IssueStatus.find
Query(IssueStatus)
.where("id = ?")
# Q 1055 : # TimeEntry.table_name
Query(TimeEntry)

# Q 1056 : # Issue.table_name
Query(Issue)

# Q 1057 : # TimeEntry.table_name
Query(TimeEntry)

# Q 1058 : # Issue.table_name
Query(Issue)

# Q 1059 : # User.current.mail
Query(User)

# Q 1060 : # User.current
Query(User)

# Q 1061 : # User.current.logged?
Query(User)

# Q 1062 : # User.current
Query(User)

# Q 1063 : # Token.delete_all(["user_id = ? AND action = ?", User.current.id, "autologin"])
Query(Token)

# Q 1064 : # Token.delete_all
Query(Token)

# Q 1065 : # User.current.id
Query(User)

# Q 1066 : # User.current
Query(User)

# Q 1067 : # @project.versions.sort
Query(Version)
.where("project_id = ?")
# Q 1068 : # @project.versions.sort
Query(Version)
.where("project_id = ?")
# Q 1069 : # @project.versions
Query(Version)
.where("project_id = ?")
# Q 1070 : # Role.find(params[:id])
Query(Role)
.where("id = ?")
# Q 1071 : # Role.find(params[:id])
Query(Role)
.where("id = ?")
# Q 1072 : # Role.find
Query(Role)
.where("id = ?")
# Q 1073 : # query.valid?
Query(Query)

# Q 1074 : # query.project
Query(Project)
.where("id = ?")
# Q 1075 : # query.statement
Query(Query)

# Q 1076 : # query.statement
Query(Query)

# Q 1077 : # @board.update_attributes(params[:board])
Query(Board)

# Q 1078 : # @board.update_attributes
Query(Board)

# Q 1079 : # @tracker.move_higher
Query(Tracker)

# Q 1080 : # self.content_type
Query(Attachment)
.select('content_type')
# Q 1081 : # self.content_type.length
Query(Attachment)
.select('content_type')
# Q 1082 : # self.content_type
Query(Attachment)
.select('content_type')
# Q 1083 : # find(:all)
Query(Repository)
.where("id = ?")
# Q 1084 : # TimeEntry.table_name
Query(TimeEntry)

# Q 1085 : # @project.id
Query(Project)

# Q 1086 : # AuthSource.find(params[:id])
Query(AuthSource)
.where("id = ?")
# Q 1087 : # AuthSource.find(params[:id])
Query(AuthSource)
.where("id = ?")
# Q 1088 : # AuthSource.find
Query(AuthSource)
.where("id = ?")
# Q 1089 : # Enumeration::get_values("IPRI")
Query(Enumeration)

# Q 1090 : # Enumeration::get_values("IPRI")
Query(Enumeration)

# Q 1091 : # Enumeration::get_values
Query(Enumeration)

# Q 1092 : # wiki.redirects.find_all_by_redirects_to(title).each(&:destroy)
Query(Wiki)

# Q 1093 : # wiki.redirects.find_all_by_redirects_to(title).each
Query(Wiki)

# Q 1094 : # wiki.redirects.find_all_by_redirects_to(title)
Query(Wiki)

# Q 1095 : # wiki.redirects.find_all_by_redirects_to
Query(Wiki)

# Q 1096 : # wiki.redirects
Query(Wiki)

# Q 1097 : # comments.scan(Regexp.new("(#{
# kw_regexp})[\s:]+(([\s,;&]*#?\\d+)+)", Regexp::IGNORECASE)).each
Query(Comment)

# Q 1098 : # comments.scan(Regexp.new("(#{
# kw_regexp})[\s:]+(([\s,;&]*#?\\d+)+)", Regexp::IGNORECASE))
Query(Comment)

# Q 1099 : # comments.scan
Query(Comment)

# Q 1100 : # Document.find(params[:id])
Query(Document)
.where("id = ?")
# Q 1101 : # Document.find(params[:id])
Query(Document)
.where("id = ?")
# Q 1102 : # Document.find
Query(Document)
.where("id = ?")
# Q 1103 : # CustomField.find(params[:id]).destroy
Query(CustomField)
.where("id = ?")
# Q 1104 : # CustomField.find(params[:id]).destroy
Query(CustomField)
.where("id = ?")
# Q 1105 : # CustomField.find(params[:id])
Query(CustomField)
.where("id = ?")
# Q 1106 : # CustomField.find
Query(CustomField)
.where("id = ?")
# Q 1107 : # @project.identifier
Query(Project)
.select('identifier')
# Q 1108 : # @issue.id
Query(Issue)

# Q 1109 : # @enumeration.move_to_top
Query(Enumeration)

# Q 1110 : # @project.issue_categories
Query(IssueCategory)
.where("project_id = ?")
# Q 1111 : # @project.issue_categories
Query(IssueCategory)
.where("project_id = ?")
# Q 1112 : # @query.destroy
Query(Query)

# Q 1113 : # ProjectCustomField.find(:all).collect
Query(ProjectCustomField)
.where("id = ?")
# Q 1114 : # ProjectCustomField.find(:all)
Query(ProjectCustomField)
.where("id = ?")
# Q 1115 : # ProjectCustomField.find
Query(ProjectCustomField)
.where("id = ?")
# Q 1116 : # CustomValue.new(:custom_field => x, :customized => @project)
Query(CustomValue)

# Q 1117 : # CustomValue.new
Query(CustomValue)

# Q 1118 : # @board.move_to_top
Query(Board)

# Q 1119 : # @tracker.move_lower
Query(Tracker)

# Q 1120 : # self.effective_date
Query(Version)
.select('effective_date')
# Q 1121 : # @document.project
Query(Project)
.where("id = ?")
# Q 1122 : # @document.project
Query(Project)
.where("id = ?")
# Q 1123 : # @custom_field.type
Query(CustomField)
.select('type')
# Q 1124 : # @issue_status.move_to_top
Query(IssueStatus)

# Q 1125 : # @project.members.collect
Query(Member)
.where("project_id = ?")
# Q 1126 : # @project.members
Query(Member)
.where("project_id = ?")
# Q 1127 : # @role.move_to_top
Query(Role)

# Q 1128 : # Journal.with_scope(:find => @find_options)
Query(Journal)

# Q 1129 : # Journal.with_scope
Query(Journal)

# Q 1130 : # @board.move_higher
Query(Board)

# Q 1131 : # @repository.scm.entry(@path, @rev)
Query(Repository)

# Q 1132 : # @repository.scm.entry(@path, @rev)
Query(Repository)

# Q 1133 : # @repository.scm.entry
Query(Repository)

# Q 1134 : # @repository.scm
Query(Repository)

# Q 1135 : # version.effective_date
Query(Version)
.select('effective_date')
# Q 1136 : # self.effective_date
Query(Version)
.select('effective_date')
# Q 1137 : # version.effective_date
Query(Version)
.select('effective_date')
# Q 1138 : # Changeset.create(:repository => self, :revision => next_rev, :scmid => revision.scmid, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1139 : # Changeset.create(:repository => self, :revision => next_rev, :scmid => revision.scmid, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1140 : # Changeset.create
Query(Changeset)

# Q 1141 : # Changeset.create(:repository => self, :revision => next_rev, :scmid => revision.scmid, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1142 : # Changeset.create
Query(Changeset)

# Q 1143 : # Changeset.create(:repository => self, :revision => next_rev, :scmid => revision.scmid, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1144 : # Changeset.create
Query(Changeset)

# Q 1145 : # Changeset.create(:repository => self, :revision => next_rev, :scmid => revision.scmid, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1146 : # Changeset.create
Query(Changeset)

# Q 1147 : # @enumeration.move_higher
Query(Enumeration)

# Q 1148 : # @project.active_children
Query(Project)

# Q 1149 : # @project.active_children
Query(Project)

# Q 1150 : # CustomField.find(params[:custom_field_ids])
Query(CustomField)
.where("id = ?")
# Q 1151 : # CustomField.find(params[:custom_field_ids])
Query(CustomField)
.where("id = ?")
# Q 1152 : # CustomField.find
Query(CustomField)
.where("id = ?")
# Q 1153 : # @board.move_lower
Query(Board)

# Q 1154 : # @tracker.move_to_bottom
Query(Tracker)

# Q 1155 : # Setting.ui_theme
Query(Setting)

# Q 1156 : # repository.project.issues.find_all_by_id(target_issue_ids)
Query(Issue)
.where("id = ?")
.where("project_id = ?")
# Q 1157 : # repository.project.issues.find_all_by_id(target_issue_ids)
Query(Issue)
.where("id = ?")
.where("project_id = ?")
# Q 1158 : # repository.project.issues.find_all_by_id
Query(Issue)
.where("id = ?")
.where("project_id = ?")
# Q 1159 : # repository.project.issues
Query(Issue)
.where("id = ?")
.where("project_id = ?")
# Q 1160 : # repository.project
Query(Project)
.where("id = ?")
# Q 1161 : # repository.project.issues.find_all_by_id(target_issue_ids)
Query(Issue)
.where("id = ?")
.where("project_id = ?")
# Q 1162 : # repository.project.issues.find_all_by_id
Query(Issue)
.where("id = ?")
.where("project_id = ?")
# Q 1163 : # repository.project.issues
Query(Issue)
.where("id = ?")
.where("project_id = ?")
# Q 1164 : # repository.project
Query(Project)
.where("id = ?")
# Q 1165 : # repository.new_record?
Query(Repository)

# Q 1166 : # @issue_status.move_higher
Query(IssueStatus)

# Q 1167 : # Setting.default_language
Query(Setting)

# Q 1168 : # @issue.status.find_new_statuses_allowed_to(logged_in_user.role_for_project(@project), @issue.tracker)
Query(IssueStatus)
.where("id = ?")
# Q 1169 : # @issue.status.find_new_statuses_allowed_to(logged_in_user.role_for_project(@project), @issue.tracker)
Query(IssueStatus)
.where("id = ?")
# Q 1170 : # @issue.status.find_new_statuses_allowed_to
Query(IssueStatus)
.where("id = ?")
# Q 1171 : # @issue.status
Query(IssueStatus)
.where("id = ?")
# Q 1172 : # @issue.tracker
Query(Tracker)
.where("id = ?")
# Q 1173 : # AuthSource.find(:all)
Query(AuthSource)
.where("id = ?")
# Q 1174 : # AuthSource.find(:all)
Query(AuthSource)
.where("id = ?")
# Q 1175 : # AuthSource.find
Query(AuthSource)
.where("id = ?")
# Q 1176 : # @role.move_higher
Query(Role)

# Q 1177 : # Journal.table_name
Query(Journal)

# Q 1178 : # Journal.table_name
Query(Journal)

# Q 1179 : # Journal.table_name
Query(Journal)

# Q 1180 : # ProjectCustomField.find(:all).collect
Query(ProjectCustomField)
.where("id = ?")
# Q 1181 : # ProjectCustomField.find(:all)
Query(ProjectCustomField)
.where("id = ?")
# Q 1182 : # ProjectCustomField.find
Query(ProjectCustomField)
.where("id = ?")
# Q 1183 : # CustomValue.new(:custom_field => x, :customized => @project, :value => (
# params[:custom_fields] ? params["custom_fields"][x.id.to_s] : nil))
Query(CustomValue)

# Q 1184 : # CustomValue.new
Query(CustomValue)

# Q 1185 : # @board.move_to_bottom
Query(Board)

# Q 1186 : # @repository.changesets_for_path(@path)
Query(Repository)

# Q 1187 : # @repository.changesets_for_path(@path)
Query(Repository)

# Q 1188 : # @repository.changesets_for_path
Query(Repository)

# Q 1189 : # self.due_date.nil?
Query(Issue)
.select('due_date')
# Q 1190 : # self.due_date
Query(Issue)
.select('due_date')
# Q 1191 : # WikiPage.pretty_title(title)
Query(WikiPage)

# Q 1192 : # WikiPage.pretty_title
Query(WikiPage)

# Q 1193 : # version.effective_date
Query(Version)
.select('effective_date')
# Q 1194 : # self.name
Query(Version)
.select('name')
# Q 1195 : # version.name
Query(Version)
.select('name')
# Q 1196 : # Change.create(:changeset => changeset, :action => change[:action], :path => change[:path], :from_path => change[:from_path], :from_revision => change[:from_revision])
Query(Change)

# Q 1197 : # Change.create
Query(Change)

# Q 1198 : # Change.create(:changeset => changeset, :action => change[:action], :path => change[:path], :from_path => change[:from_path], :from_revision => change[:from_revision])
Query(Change)

# Q 1199 : # Change.create(:changeset => changeset, :action => change[:action], :path => change[:path], :from_path => change[:from_path], :from_revision => change[:from_revision])
Query(Change)

# Q 1200 : # Change.create(:changeset => changeset, :action => change[:action], :path => change[:path], :from_path => change[:from_path], :from_revision => change[:from_revision])
Query(Change)

# Q 1201 : # find(:all)
Query(Repository)
.where("id = ?")
# Q 1202 : # news.project.recipients
Query(Project)
.where("id = ?")
# Q 1203 : # news.project
Query(Project)
.where("id = ?")
# Q 1204 : # news.project.recipients
Query(Project)
.where("id = ?")
# Q 1205 : # news.project
Query(Project)
.where("id = ?")
# Q 1206 : # @enumeration.move_lower
Query(Enumeration)

# Q 1207 : # Issue.table_name
Query(Issue)

# Q 1208 : # find(*args)
Query(User)
.where("id = ?")
# Q 1209 : # find(*args)
Query(User)
.where("id = ?")
# Q 1210 : # news.project.name
Query(Project)
.where("id = ?")
.select('name')
# Q 1211 : # news.project
Query(Project)
.where("id = ?")
# Q 1212 : # news.title
Query(News)
.select('title')
# Q 1213 : # news.project.name
Query(Project)
.where("id = ?")
.select('name')
# Q 1214 : # news.project
Query(Project)
.where("id = ?")
# Q 1215 : # news.title
Query(News)
.select('title')
# Q 1216 : # @issue_status.move_lower
Query(IssueStatus)

# Q 1217 : # Setting.lost_password?
Query(Setting)

# Q 1218 : # @role.move_lower
Query(Role)

# Q 1219 : # @project.save
Query(Project)

# Q 1220 : # self.relation_type
Query(IssueRelation)
.select('relation_type')
# Q 1221 : # self.host
Query(AuthSourceLdap)
.select('host')
# Q 1222 : # self.filename?
Query(Attachment)

# Q 1223 : # self.revision
Query(Changeset)
.select('revision')
# Q 1224 : # self.revision
Query(Changeset)
.select('revision')
# Q 1225 : # self.revision
Query(Changeset)
.select('revision')
# Q 1226 : # self.revision
Query(Changeset)
.select('revision')
# Q 1227 : # @user.memberships.length
Query(Member)
.where("user_id = ?")
# Q 1228 : # @user.memberships
Query(Member)
.where("user_id = ?")
# Q 1229 : # @enumeration.move_to_bottom
Query(Enumeration)

# Q 1230 : # @project.name
Query(Project)
.select('name')
# Q 1231 : # Setting.app_title
Query(Setting)

# Q 1232 : # query.name
Query(Query)
.select('name')
# Q 1233 : # self.port
Query(AuthSourceLdap)
.select('port')
# Q 1234 : # Issue.table_name
Query(Issue)

# Q 1235 : # repository.root_url.blank?
Query(Repository)
.select('root_url')
# Q 1236 : # repository.root_url
Query(Repository)
.select('root_url')
# Q 1237 : # Setting.date_format.to_i
Query(Setting)

# Q 1238 : # Setting.date_format
Query(Setting)

# Q 1239 : # @issue_status.move_to_bottom
Query(IssueStatus)

# Q 1240 : # @user.mail_notification?
Query(User)

# Q 1241 : # @user.notified_projects_ids.empty?
Query(User)

# Q 1242 : # @user.notified_projects_ids
Query(User)

# Q 1243 : # Token.find_by_action_and_value("recovery", params[:token])
Query(Token)
.where(" = ?")
.where("action = ?")
.where("value = ?")
# Q 1244 : # Token.find_by_action_and_value("recovery", params[:token])
Query(Token)
.where(" = ?")
.where("action = ?")
.where("value = ?")
# Q 1245 : # Token.find_by_action_and_value
Query(Token)
.where("action = ?")
.where("value = ?")
# Q 1246 : # User.find(params[:id])
Query(User)
.where("id = ?")
# Q 1247 : # User.find(params[:id])
Query(User)
.where("id = ?")
# Q 1248 : # User.find
Query(User)
.where("id = ?")
# Q 1249 : # @role.move_to_bottom
Query(Role)

# Q 1250 : # Query.find(params[:id])
Query(Query)
.where("id = ?")
# Q 1251 : # Query.find(params[:id])
Query(Query)
.where("id = ?")
# Q 1252 : # Query.find
Query(Query)
.where("id = ?")
# Q 1253 : # @repository.changesets.count
Query(Changeset)
.where("repository_id = ?")
# Q 1254 : # @repository.changesets.count
Query(Changeset)
.where("repository_id = ?")
# Q 1255 : # @repository.changesets
Query(Changeset)
.where("repository_id = ?")
# Q 1256 : # self.due_date
Query(Issue)
.select('due_date')
# Q 1257 : # self.start_date
Query(Issue)
.select('start_date')
# Q 1258 : # self.due_date
Query(Issue)
.select('due_date')
# Q 1259 : # self.start_date
Query(Issue)
.select('start_date')
# Q 1260 : # version.to_i
Query(Version)

# Q 1261 : # self.builtin
Query(Role)
.select('builtin')
# Q 1262 : # User.current.logged?
Query(User)

# Q 1263 : # User.current
Query(User)

# Q 1264 : # @token.expired?
Query(Token)

# Q 1265 : # Tracker.find(params[:id])
Query(Tracker)
.where("id = ?")
# Q 1266 : # Tracker.find(params[:id])
Query(Tracker)
.where("id = ?")
# Q 1267 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 1268 : # self.tls
Query(AuthSourceLdap)
.select('tls')
# Q 1269 : # issue.status.is_closed?
Query(IssueStatus)
.where("id = ?")
# Q 1270 : # issue.status
Query(IssueStatus)
.where("id = ?")
# Q 1271 : # issue.status.is_closed?
Query(IssueStatus)
.where("id = ?")
# Q 1272 : # issue.status
Query(IssueStatus)
.where("id = ?")
# Q 1273 : # next if issue.status.is_closed?
Query(Issue)

# Q 1274 : # next if issue.status.is_closed?
Query(Issue)

# Q 1275 : # changeset.new_record?
Query(Changeset)

# Q 1276 : # changeset.new_record?
Query(Changeset)

# Q 1277 : # next if changeset.new_record?
Query(Changeset)

# Q 1278 : # next if changeset.new_record?
Query(Changeset)

# Q 1279 : # self.builtin
Query(Role)
.select('builtin')
# Q 1280 : # Enumeration::get_values("IPRI")
Query(Enumeration)

# Q 1281 : # Enumeration::get_values("IPRI")
Query(Enumeration)

# Q 1282 : # Enumeration::get_values
Query(Enumeration)

# Q 1283 : # User.find(:first, :conditions => ["login=? and hashed_password=?", "admin", User.hash_password("admin")]).nil?
Query(User)
.where("id = ?")
.where("login = ?")
.where("hashed_password = ?")
.where("id = ?")
# Q 1284 : # User.find(:first, :conditions => ["login=? and hashed_password=?", "admin", User.hash_password("admin")])
Query(User)
.where("id = ?")
.where("login = ?")
.where("hashed_password = ?")
.where("id = ?")
# Q 1285 : # User.find
Query(User)
.where("id = ?")
# Q 1286 : # User.hash_password("admin")
Query(User)

# Q 1287 : # User.hash_password
Query(User)

# Q 1288 : # @token.user
Query(User)
.where("id = ?")
# Q 1289 : # @token.user
Query(User)
.where("id = ?")
# Q 1290 : # UserCustomField.find(:all).collect
Query(UserCustomField)
.where("id = ?")
# Q 1291 : # UserCustomField.find(:all)
Query(UserCustomField)
.where("id = ?")
# Q 1292 : # UserCustomField.find
Query(UserCustomField)
.where("id = ?")
# Q 1293 : # @user.custom_values.find_by_custom_field_id(x.id)
Query(CustomValue)
.where("user_id = ?")
# Q 1294 : # @user.custom_values.find_by_custom_field_id
Query(CustomValue)
.where("user_id = ?")
# Q 1295 : # @user.custom_values
Query(CustomValue)
.where("user_id = ?")
# Q 1296 : # CustomValue.new(:custom_field => x)
Query(CustomValue)

# Q 1297 : # CustomValue.new
Query(CustomValue)

# Q 1298 : # @query.project
Query(Project)
.where("id = ?")
# Q 1299 : # @query.project
Query(Project)
.where("id = ?")
# Q 1300 : # @tracker.issues.empty?
Query(Issue)
.where("tracker_id = ?")
# Q 1301 : # @tracker.issues
Query(Issue)
.where("tracker_id = ?")
# Q 1302 : # self.fixed_issues.find(:first)
Query(Issue)
.where("version_id = ?")
.where("id = ?")
# Q 1303 : # self.fixed_issues.find
Query(Issue)
.where("version_id = ?")
.where("id = ?")
# Q 1304 : # self.fixed_issues
Query(Issue)
.where("version_id = ?")
# Q 1305 : # Attachment.find_by_id(detail.prop_key)
Query(Attachment)

# Q 1306 : # Attachment.find_by_id
Query(Attachment)

# Q 1307 : # AuthSource.find(params[:id])
Query(AuthSource)
.where("id = ?")
# Q 1308 : # AuthSource.find(params[:id])
Query(AuthSource)
.where("id = ?")
# Q 1309 : # AuthSource.find
Query(AuthSource)
.where("id = ?")
# Q 1310 : # Attachment.storage_path
Query(Attachment)

# Q 1311 : # @query.editable_by?(logged_in_user)
Query(Query)

# Q 1312 : # @query.editable_by?
Query(Query)

# Q 1313 : # @board.destroy
Query(Board)

# Q 1314 : # self.relation_type
Query(IssueRelation)
.select('relation_type')
# Q 1315 : # find(:first, :conditions => ["login=?", login])
Query(User)
.where("login = ?")
.where("id = ?")
.where("id = ?")
# Q 1316 : # find(:first, :conditions => ["login=?", login])
Query(User)
.where("login = ?")
.where("id = ?")
.where("id = ?")
# Q 1317 : # repository.new_record?
Query(Repository)

# Q 1318 : # @project.custom_fields_for_issues(@issue.tracker).collect
Query(Project)

# Q 1319 : # @project.custom_fields_for_issues(@issue.tracker)
Query(Project)

# Q 1320 : # @project.custom_fields_for_issues
Query(Project)

# Q 1321 : # @issue.tracker
Query(Tracker)
.where("id = ?")
# Q 1322 : # @issue.custom_values.find_by_custom_field_id(x.id)
Query(CustomValue)
.where("issue_id = ?")
# Q 1323 : # @issue.custom_values.find_by_custom_field_id
Query(CustomValue)
.where("issue_id = ?")
# Q 1324 : # @issue.custom_values
Query(CustomValue)
.where("issue_id = ?")
# Q 1325 : # CustomValue.new(:custom_field => x, :customized => @issue)
Query(CustomValue)

# Q 1326 : # CustomValue.new
Query(CustomValue)

# Q 1327 : # @auth_source.users.find(:first)
Query(User)
.where("auth_source_id = ?")
.where("id = ?")
# Q 1328 : # @auth_source.users.find
Query(User)
.where("auth_source_id = ?")
.where("id = ?")
# Q 1329 : # @auth_source.users
Query(User)
.where("auth_source_id = ?")
# Q 1330 : # @repository.changesets.find(:all, :limit => @changeset_pages.items_per_page, :offset => @changeset_pages.current.offset)
Query(Changeset)
.where("repository_id = ?")
.where("id = ?")
# Q 1331 : # @repository.changesets.find(:all, :limit => @changeset_pages.items_per_page, :offset => @changeset_pages.current.offset)
Query(Changeset)
.where("repository_id = ?")
.where("id = ?")
# Q 1332 : # @repository.changesets.find
Query(Changeset)
.where("repository_id = ?")
.where("id = ?")
# Q 1333 : # @repository.changesets
Query(Changeset)
.where("repository_id = ?")
# Q 1334 : # issue.save
Query(Issue)

# Q 1335 : # issue.save
Query(Issue)

# Q 1336 : # issue.save
Query(Issue)

# Q 1337 : # issue.save
Query(Issue)

# Q 1338 : # Change.create(:changeset => changeset, :action => change[:action], :path => change[:path], :from_path => change[:from_path], :from_revision => change[:from_revision])
Query(Change)

# Q 1339 : # Change.create
Query(Change)

# Q 1340 : # Change.create(:changeset => changeset, :action => change[:action], :path => change[:path], :from_path => change[:from_path], :from_revision => change[:from_revision])
Query(Change)

# Q 1341 : # Change.create
Query(Change)

# Q 1342 : # Change.create(:changeset => changeset, :action => change[:action], :path => change[:path], :from_path => change[:from_path], :from_revision => change[:from_revision])
Query(Change)

# Q 1343 : # Change.create(:changeset => changeset, :action => change[:action], :path => change[:path], :from_path => change[:from_path], :from_revision => change[:from_revision])
Query(Change)

# Q 1344 : # Change.create(:changeset => changeset, :action => change[:action], :path => change[:path], :from_path => change[:from_path], :from_revision => change[:from_revision])
Query(Change)

# Q 1345 : # message.board.project.name
Query(Project)
.where("id = ?")
.where("id = ?")
.select('name')
# Q 1346 : # message.board.project
Query(Project)
.where("id = ?")
.where("id = ?")
# Q 1347 : # message.board
Query(Board)
.where("id = ?")
# Q 1348 : # message.board.name
Query(Board)
.where("id = ?")
.select('name')
# Q 1349 : # message.board
Query(Board)
.where("id = ?")
# Q 1350 : # message.subject
Query(Message)
.select('subject')
# Q 1351 : # message.board.project.name
Query(Project)
.where("id = ?")
.where("id = ?")
.select('name')
# Q 1352 : # message.board.project
Query(Project)
.where("id = ?")
.where("id = ?")
# Q 1353 : # message.board
Query(Board)
.where("id = ?")
# Q 1354 : # message.board.name
Query(Board)
.where("id = ?")
.select('name')
# Q 1355 : # message.board
Query(Board)
.where("id = ?")
# Q 1356 : # message.subject
Query(Message)
.select('subject')
# Q 1357 : # repository.new_record?
Query(Repository)

# Q 1358 : # @auth_source.destroy
Query(AuthSource)

# Q 1359 : # Enumeration.find(params[:id]).destroy
Query(Enumeration)
.where("id = ?")
# Q 1360 : # Enumeration.find(params[:id])
Query(Enumeration)
.where("id = ?")
# Q 1361 : # Enumeration.find
Query(Enumeration)
.where("id = ?")
# Q 1362 : # @user.save
Query(User)

# Q 1363 : # Project.find(params[:project_id])
Query(Project)
.where("id = ?")
# Q 1364 : # Project.find(params[:project_id])
Query(Project)
.where("id = ?")
# Q 1365 : # Project.find
Query(Project)
.where("id = ?")
# Q 1366 : # @tracker.destroy
Query(Tracker)

# Q 1367 : # self.disk_filename
Query(Attachment)
.select('disk_filename')
# Q 1368 : # Setting.date_format.to_i
Query(Setting)

# Q 1369 : # Setting.date_format
Query(Setting)

# Q 1370 : # IssueStatus.find(params[:id]).destroy
Query(IssueStatus)
.where("id = ?")
# Q 1371 : # IssueStatus.find(params[:id])
Query(IssueStatus)
.where("id = ?")
# Q 1372 : # IssueStatus.find
Query(IssueStatus)
.where("id = ?")
# Q 1373 : # @user.auth_source_id
Query(User)
.select('auth_source_id')
# Q 1374 : # @token.destroy
Query(Token)

# Q 1375 : # @user.auth_source_id
Query(User)
.select('auth_source_id')
# Q 1376 : # Role.find_by_id(params[:role_id])
Query(Role)

# Q 1377 : # Role.find_by_id(params[:role_id])
Query(Role)

# Q 1378 : # Role.find_by_id
Query(Role)

# Q 1379 : # self.content.version
Query(WikiContent)
.where("id = ?")
.select('version')
# Q 1380 : # self.content
Query(WikiContent)
.where("id = ?")
# Q 1381 : # user.active?
Query(User)

# Q 1382 : # message.board_id
Query(Message)
.select('board_id')
# Q 1383 : # message.root
Query(Message)

# Q 1384 : # message.board_id
Query(Message)
.select('board_id')
# Q 1385 : # message.root
Query(Message)

# Q 1386 : # @issue.init_journal(self.logged_in_user)
Query(Issue)

# Q 1387 : # @issue.init_journal
Query(Issue)

# Q 1388 : # Tracker.find_by_id(params[:tracker_id])
Query(Tracker)

# Q 1389 : # Tracker.find_by_id(params[:tracker_id])
Query(Tracker)

# Q 1390 : # Tracker.find_by_id
Query(Tracker)

# Q 1391 : # User.find_by_rss_key(params[:key])
Query(User)

# Q 1392 : # User.find_by_rss_key(params[:key])
Query(User)

# Q 1393 : # User.find_by_rss_key
Query(User)

# Q 1394 : # user.auth_source
Query(AuthSource)
.where("id = ?")
# Q 1395 : # find(:all, :conditions => { :builtin => 0 }, :order => "position")
Query(Role)
.where("id = ?")
# Q 1396 : # @user.check_password?(params[:password])
Query(User)

# Q 1397 : # @user.check_password?
Query(User)

# Q 1398 : # UserCustomField.find(:all).collect
Query(UserCustomField)
.where("id = ?")
# Q 1399 : # UserCustomField.find(:all)
Query(UserCustomField)
.where("id = ?")
# Q 1400 : # UserCustomField.find
Query(UserCustomField)
.where("id = ?")
# Q 1401 : # CustomValue.new(:custom_field => x, :customized => @user, :value => params["custom_fields"][x.id.to_s])
Query(CustomValue)

# Q 1402 : # CustomValue.new
Query(CustomValue)

# Q 1403 : # Tracker.find(:all)
Query(Tracker)
.where("id = ?")
# Q 1404 : # Tracker.find(:all)
Query(Tracker)
.where("id = ?")
# Q 1405 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 1406 : # Setting.login_required?
Query(Setting)

# Q 1407 : # @project.custom_values.find(:all, :include => :custom_field)
Query(CustomValue)
.where("project_id = ?")
.where("id = ?")
# Q 1408 : # @project.custom_values.find(:all, :include => :custom_field)
Query(CustomValue)
.where("project_id = ?")
.where("id = ?")
# Q 1409 : # @project.custom_values.find
Query(CustomValue)
.where("project_id = ?")
.where("id = ?")
# Q 1410 : # @project.custom_values
Query(CustomValue)
.where("project_id = ?")
# Q 1411 : # find(:all, :limit => count, :conditions => visible_by(user), :order => "created_on DESC")
Query(Project)
.where("id = ?")
# Q 1412 : # @project.members.find(:all, :include => [:user, :role], :order => "position").group_by
Query(Member)
.where("project_id = ?")
.where("id = ?")
# Q 1413 : # @project.members.find(:all, :include => [:user, :role], :order => "position")
Query(Member)
.where("project_id = ?")
.where("id = ?")
# Q 1414 : # @project.members.find
Query(Member)
.where("project_id = ?")
.where("id = ?")
# Q 1415 : # @project.members
Query(Member)
.where("project_id = ?")
# Q 1416 : # Project.find(params[:project_id])
Query(Project)
.where("id = ?")
# Q 1417 : # Project.find(params[:project_id])
Query(Project)
.where("id = ?")
# Q 1418 : # Project.find
Query(Project)
.where("id = ?")
# Q 1419 : # user.auth_source.authenticate(login, password)
Query(AuthSource)
.where("id = ?")
# Q 1420 : # user.auth_source.authenticate
Query(AuthSource)
.where("id = ?")
# Q 1421 : # user.auth_source
Query(AuthSource)
.where("id = ?")
# Q 1422 : # @project.custom_fields_for_issues(@issue.tracker).collect
Query(Project)

# Q 1423 : # @project.custom_fields_for_issues(@issue.tracker)
Query(Project)

# Q 1424 : # @project.custom_fields_for_issues
Query(Project)

# Q 1425 : # @issue.tracker
Query(Tracker)
.where("id = ?")
# Q 1426 : # CustomValue.new(:custom_field => x, :customized => @issue, :value => params["custom_fields"][x.id.to_s])
Query(CustomValue)

# Q 1427 : # CustomValue.new
Query(CustomValue)

# Q 1428 : # @user.save
Query(User)

# Q 1429 : # @trackers.collect
Query(Tracker)

# Q 1430 : # Workflow.destroy_all(["role_id=? and tracker_id=?", @role.id, @tracker.id])
Query(Workflow)

# Q 1431 : # Workflow.destroy_all
Query(Workflow)

# Q 1432 : # @role.id
Query(Role)

# Q 1433 : # @tracker.id
Query(Tracker)

# Q 1434 : # @project.active_children
Query(Project)

# Q 1435 : # @project.active_children
Query(Project)

# Q 1436 : # @project.boards.find(params[:id])
Query(Board)
.where("project_id = ?")
.where("id = ?")
# Q 1437 : # @project.boards.find(params[:id])
Query(Board)
.where("project_id = ?")
.where("id = ?")
# Q 1438 : # @project.boards.find
Query(Board)
.where("project_id = ?")
.where("id = ?")
# Q 1439 : # @project.boards
Query(Board)
.where("project_id = ?")
# Q 1440 : # @project.name
Query(Project)
.select('name')
# Q 1441 : # @project.name
Query(Project)
.select('name')
# Q 1442 : # user.language
Query(User)
.select('language')
# Q 1443 : # user.language
Query(User)
.select('language')
# Q 1444 : # User.current.admin?
Query(User)

# Q 1445 : # User.current
Query(User)

# Q 1446 : # @user.update_attributes(params[:user])
Query(User)

# Q 1447 : # @user.update_attributes
Query(User)

# Q 1448 : # @project.news.find(:all, :limit => 5, :include => [:author, :project], :order => "News.created_on DESC")
Query(News)
.where("project_id = ?")
.where("id = ?")
# Q 1449 : # @project.news.find(:all, :limit => 5, :include => [:author, :project], :order => "News.created_on DESC")
Query(News)
.where("project_id = ?")
.where("id = ?")
# Q 1450 : # @project.news.find
Query(News)
.where("project_id = ?")
.where("id = ?")
# Q 1451 : # @project.news
Query(News)
.where("project_id = ?")
# Q 1452 : # News.table_name
Query(News)

# Q 1453 : # Setting.maximum(:updated_on)
Query(Setting)

# Q 1454 : # Setting.maximum(:updated_on)
Query(Setting)

# Q 1455 : # Setting.maximum
Query(Setting)

# Q 1456 : # user.mail
Query(User)

# Q 1457 : # user.mail
Query(User)

# Q 1458 : # @wiki.find_page(params[:page])
Query(Wiki)

# Q 1459 : # @wiki.find_page(params[:page])
Query(Wiki)

# Q 1460 : # @wiki.find_page
Query(Wiki)

# Q 1461 : # news.each
Query(News)

# Q 1462 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 1463 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 1464 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 1465 : # user.admin?
Query(User)

# Q 1466 : # User.hash_password(password)
Query(User)

# Q 1467 : # User.hash_password
Query(User)

# Q 1468 : # user.hashed_password
Query(User)
.select('hashed_password')
# Q 1469 : # changesets.maximum(:committed_on)
Query(Changeset)

# Q 1470 : # changesets.maximum(:committed_on)
Query(Changeset)

# Q 1471 : # changesets.maximum
Query(Changeset)

# Q 1472 : # find(:first, :conditions => { :builtin => BUILTIN_NON_MEMBER })
Query(Role)
.where("id = ?")
# Q 1473 : # @role.workflows.build(:tracker_id => @tracker.id, :old_status_id => old, :new_status_id => new)
Query(Workflow)
.where("role_id = ?")
# Q 1474 : # @role.workflows.build
Query(Workflow)
.where("role_id = ?")
# Q 1475 : # @role.workflows
Query(Workflow)
.where("role_id = ?")
# Q 1476 : # @tracker.id
Query(Tracker)

# Q 1477 : # Issue.count(:group => :tracker, :joins => "INNER JOIN IssueStatus ON IssueStatus.id = Issue.status_id", :conditions => ["project_id=? and IssueStatus.is_closed=?", @project.id, false])
Query(Issue)

# Q 1478 : # Issue.count(:group => :tracker, :joins => "INNER JOIN IssueStatus ON IssueStatus.id = Issue.status_id", :conditions => ["project_id=? and IssueStatus.is_closed=?", @project.id, false])
Query(Issue)

# Q 1479 : # Issue.count
Query(Issue)

# Q 1480 : # IssueStatus.table_name
Query(IssueStatus)

# Q 1481 : # IssueStatus.table_name
Query(IssueStatus)

# Q 1482 : # Issue.table_name
Query(Issue)

# Q 1483 : # IssueStatus.table_name
Query(IssueStatus)

# Q 1484 : # @project.id
Query(Project)

# Q 1485 : # WikiDiff.new(content_to, content_from)
Query(WikiDiff)

# Q 1486 : # WikiDiff.new
Query(WikiDiff)

# Q 1487 : # Project.table_name
Query(Project)

# Q 1488 : # @issue.save
Query(Issue)

# Q 1489 : # Issue.count(:group => :tracker, :conditions => ["project_id=?", @project.id])
Query(Issue)

# Q 1490 : # Issue.count(:group => :tracker, :conditions => ["project_id=?", @project.id])
Query(Issue)

# Q 1491 : # Issue.count
Query(Issue)

# Q 1492 : # @project.id
Query(Project)

# Q 1493 : # find(:all, :limit => 5, :order => "downloads DESC")
Query(Attachment)
.where("id = ?")
# Q 1494 : # user.memberships.any?
Query(Member)
.where("user_id = ?")
# Q 1495 : # user.memberships
Query(Member)
.where("user_id = ?")
# Q 1496 : # Project.find(params[:project_id])
Query(Project)
.where("id = ?")
# Q 1497 : # Project.find(params[:project_id])
Query(Project)
.where("id = ?")
# Q 1498 : # Project.find
Query(Project)
.where("id = ?")
# Q 1499 : # @project.time_entries.sum(:hours)
Query(TimeEntry)
.where("project_id = ?")
# Q 1500 : # @project.time_entries.sum(:hours)
Query(TimeEntry)
.where("project_id = ?")
# Q 1501 : # @project.time_entries.sum
Query(TimeEntry)
.where("project_id = ?")
# Q 1502 : # @project.time_entries
Query(TimeEntry)
.where("project_id = ?")
# Q 1503 : # @repository.scm.cat(@path, @rev)
Query(Repository)

# Q 1504 : # @repository.scm.cat(@path, @rev)
Query(Repository)

# Q 1505 : # @repository.scm.cat
Query(Repository)

# Q 1506 : # @repository.scm
Query(Repository)

# Q 1507 : # Project.table_name
Query(Project)

# Q 1508 : # Project.table_name
Query(Project)

# Q 1509 : # Project.table_name
Query(Project)

# Q 1510 : # user.memberships.collect { |m|
#   
#   m.project_id
# }.join(",")
Query(Member)
.where("user_id = ?")
# Q 1511 : # user.memberships.collect { |m|
#   
#   m.project_id
# }.join
Query(Member)
.where("user_id = ?")
# Q 1512 : # user.memberships.collect
Query(Member)
.where("user_id = ?")
# Q 1513 : # user.memberships
Query(Member)
.where("user_id = ?")
# Q 1514 : # User.find_by_mail(params[:mail])
Query(User)

# Q 1515 : # User.find_by_mail(params[:mail])
Query(User)

# Q 1516 : # User.find_by_mail
Query(User)

# Q 1517 : # AuthSource.find(:all)
Query(AuthSource)
.where("id = ?")
# Q 1518 : # AuthSource.find(:all)
Query(AuthSource)
.where("id = ?")
# Q 1519 : # AuthSource.find
Query(AuthSource)
.where("id = ?")
# Q 1520 : # @role.save
Query(Role)

# Q 1521 : # @project.is_public?
Query(Project)

# Q 1522 : # @user.role_for_project(@project)
Query(User)

# Q 1523 : # @user.role_for_project
Query(User)

# Q 1524 : # User.current.rss_key
Query(Token)
.where("id = ?")
# Q 1525 : # User.current.rss_key
Query(Token)
.where("id = ?")
# Q 1526 : # User.current
Query(User)

# Q 1527 : # AuthSource.authenticate(login, password)
Query(AuthSource)

# Q 1528 : # AuthSource.authenticate(login, password)
Query(AuthSource)

# Q 1529 : # AuthSource.authenticate
Query(AuthSource)

# Q 1530 : # Project.with_scope(:find => { :conditions => Project.visible_by(logged_in_user) })
Query(Project)

# Q 1531 : # Project.with_scope
Query(Project)

# Q 1532 : # Project.visible_by(logged_in_user)
Query(Project)

# Q 1533 : # Project.visible_by
Query(Project)

# Q 1534 : # Role.find_all_givable
Query(Role)

# Q 1535 : # Role.find_all_givable
Query(Role)

# Q 1536 : # Project.table_name
Query(Project)

# Q 1537 : # Project.table_name
Query(Project)

# Q 1538 : # Project.table_name
Query(Project)

# Q 1539 : # find(:first, :conditions => { :builtin => BUILTIN_ANONYMOUS })
Query(Role)
.where("id = ?")
# Q 1540 : # Project.find(:all, :limit => limit, :conditions => [(
# ["(LOWER(name) like ? OR LOWER(description) like ?)"] * like_tokens.size).join(operator), *(
# like_tokens * 2).sort])
Query(Project)
.where("id = ?")
# Q 1541 : # Project.find
Query(Project)
.where("id = ?")
# Q 1542 : # Project.find(:all, :limit => limit, :conditions => [(
# ["(LOWER(name) like ? OR LOWER(description) like ?)"] * like_tokens.size).join(operator), *(
# like_tokens * 2).sort])
Query(Project)
.where("id = ?")
# Q 1543 : # Project.find
Query(Project)
.where("id = ?")
# Q 1544 : # Project.find(:all, :order => "name", :conditions => "status=#{
# Project::STATUS_ACTIVE}")
Query(Project)
.where("id = ?")
# Q 1545 : # Project.find
Query(Project)
.where("id = ?")
# Q 1546 : # @user.projects
Query(Project)
.where("user_id = ?")
# Q 1547 : # Member.new
Query(Member)

# Q 1548 : # Issue.column_names
Query(Issue)

# Q 1549 : # token.user.language
Query(User)
.where("id = ?")
.select('language')
# Q 1550 : # token.user
Query(User)
.where("id = ?")
# Q 1551 : # token.user.language
Query(User)
.where("id = ?")
.select('language')
# Q 1552 : # token.user
Query(User)
.where("id = ?")
# Q 1553 : # User.current.allowed_to?({ :controller => ctrl, :action => action }, @project)
Query(User)

# Q 1554 : # User.current.allowed_to?({ :controller => ctrl, :action => action }, @project)
Query(User)

# Q 1555 : # User.current.allowed_to?
Query(User)

# Q 1556 : # User.current
Query(User)

# Q 1557 : # user.auth_source_id
Query(User)
.select('auth_source_id')
# Q 1558 : # Project.table_name
Query(Project)

# Q 1559 : # Project::find(:all, :conditions => ["parent_id IS NULL AND status = #{
# Project::STATUS_ACTIVE} AND id <> ?", @project.id])
Query(Project)
.where("id = ?")
.where("parent_id = ?")
.where("status = ?")
.where("id = ?")
.where("id = ?")
# Q 1560 : # Project::find(:all, :conditions => ["parent_id IS NULL AND status = #{
# Project::STATUS_ACTIVE} AND id <> ?", @project.id])
Query(Project)
.where("id = ?")
.where("parent_id = ?")
.where("status = ?")
.where("id = ?")
.where("id = ?")
# Q 1561 : # Project::find
Query(Project)
.where("id = ?")
# Q 1562 : # @project.id
Query(Project)

# Q 1563 : # JournalDetail.new(:property => "attr", :prop_key => c, :old_value => @issue_before_change.send(c), :value => send(c))
Query(JournalDetail)

# Q 1564 : # JournalDetail.new
Query(JournalDetail)

# Q 1565 : # Setting.default_language
Query(Setting)

# Q 1566 : # Setting.default_language
Query(Setting)

# Q 1567 : # token.user.mail
Query(User)
.where("id = ?")
# Q 1568 : # token.user
Query(User)
.where("id = ?")
# Q 1569 : # token.user.mail
Query(User)
.where("id = ?")
# Q 1570 : # token.user
Query(User)
.where("id = ?")
# Q 1571 : # User.current.logged?
Query(User)

# Q 1572 : # User.current
Query(User)

# Q 1573 : # Role.find(:all, :order => "builtin, position")
Query(Role)
.where("id = ?")
# Q 1574 : # Role.find(:all, :order => "builtin, position")
Query(Role)
.where("id = ?")
# Q 1575 : # Role.find
Query(Role)
.where("id = ?")
# Q 1576 : # IssueCustomField.find(:all)
Query(IssueCustomField)
.where("id = ?")
# Q 1577 : # IssueCustomField.find(:all)
Query(IssueCustomField)
.where("id = ?")
# Q 1578 : # IssueCustomField.find
Query(IssueCustomField)
.where("id = ?")
# Q 1579 : # wiki.project
Query(Project)
.where("id = ?")
# Q 1580 : # User.current.rss_token
Query(User)

# Q 1581 : # User.current
Query(User)

# Q 1582 : # Token.new(:user => user, :action => "recovery")
Query(Token)

# Q 1583 : # Token.new(:user => user, :action => "recovery")
Query(Token)

# Q 1584 : # Token.new
Query(Token)

# Q 1585 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 1586 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 1587 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 1588 : # Setting.feeds_limit.to_i
Query(Setting)

# Q 1589 : # Setting.feeds_limit
Query(Setting)

# Q 1590 : # IssueCategory.new
Query(IssueCategory)

# Q 1591 : # self.filename
Query(Attachment)
.select('filename')
# Q 1592 : # self.status
Query(Project)
.select('status')
# Q 1593 : # find(:first, :conditions => ["login=?", login])
Query(User)
.where("login = ?")
.where("id = ?")
.where("id = ?")
# Q 1594 : # find(:first, :conditions => ["login=?", login])
Query(User)
.where("login = ?")
.where("id = ?")
.where("id = ?")
# Q 1595 : # User.current.rss_token.destroy
Query(User)

# Q 1596 : # User.current.rss_token
Query(User)

# Q 1597 : # User.current
Query(User)

# Q 1598 : # @tokens.join(" ")
Query(Token)

# Q 1599 : # @tokens.join(" ")
Query(Token)

# Q 1600 : # @tokens.join
Query(Token)

# Q 1601 : # token.save
Query(Token)

# Q 1602 : # User.find(params[:id])
Query(User)
.where("id = ?")
# Q 1603 : # User.find(params[:id])
Query(User)
.where("id = ?")
# Q 1604 : # User.find
Query(User)
.where("id = ?")
# Q 1605 : # IssueStatus.find(:all, :include => :workflows, :order => "position")
Query(IssueStatus)
.where("id = ?")
# Q 1606 : # IssueStatus.find(:all, :include => :workflows, :order => "position")
Query(IssueStatus)
.where("id = ?")
# Q 1607 : # IssueStatus.find
Query(IssueStatus)
.where("id = ?")
# Q 1608 : # @project.members.new
Query(Member)
.where("project_id = ?")
# Q 1609 : # @project.members
Query(Member)
.where("project_id = ?")
# Q 1610 : # @repository.changesets.find_by_revision(@rev)
Query(Changeset)
.where("repository_id = ?")
# Q 1611 : # @repository.changesets.find_by_revision(@rev)
Query(Changeset)
.where("repository_id = ?")
# Q 1612 : # @repository.changesets.find_by_revision
Query(Changeset)
.where("repository_id = ?")
# Q 1613 : # @repository.changesets
Query(Changeset)
.where("repository_id = ?")
# Q 1614 : # user.language
Query(User)
.select('language')
# Q 1615 : # user.login
Query(User)
.select('login')
# Q 1616 : # token.value
Query(Token)
.select('value')
# Q 1617 : # token.value
Query(Token)
.select('value')
# Q 1618 : # @wiki.find_page(params[:page])
Query(Wiki)

# Q 1619 : # @wiki.find_page(params[:page])
Query(Wiki)

# Q 1620 : # @wiki.find_page
Query(Wiki)

# Q 1621 : # Member.find(params[:membership_id])
Query(Member)
.where("id = ?")
# Q 1622 : # Member.find
Query(Member)
.where("id = ?")
# Q 1623 : # Member.new(:user => @user)
Query(Member)

# Q 1624 : # Member.new
Query(Member)

# Q 1625 : # ProjectCustomField.find(:all).collect
Query(ProjectCustomField)
.where("id = ?")
# Q 1626 : # ProjectCustomField.find(:all)
Query(ProjectCustomField)
.where("id = ?")
# Q 1627 : # ProjectCustomField.find
Query(ProjectCustomField)
.where("id = ?")
# Q 1628 : # @project.custom_values.find_by_custom_field_id(x.id)
Query(CustomValue)
.where("project_id = ?")
# Q 1629 : # @project.custom_values.find_by_custom_field_id
Query(CustomValue)
.where("project_id = ?")
# Q 1630 : # @project.custom_values
Query(CustomValue)
.where("project_id = ?")
# Q 1631 : # CustomValue.new(:custom_field => x)
Query(CustomValue)

# Q 1632 : # CustomValue.new
Query(CustomValue)

# Q 1633 : # @project.repository
Query(Repository)
.where("id = ?")
# Q 1634 : # @changeset.changes.size
Query(Change)
.where("changeset_id = ?")
# Q 1635 : # @changeset.changes.size
Query(Change)
.where("changeset_id = ?")
# Q 1636 : # @changeset.changes
Query(Change)
.where("changeset_id = ?")
# Q 1637 : # @issue.init_journal(User.current, params[:notes])
Query(Issue)

# Q 1638 : # @issue.init_journal(User.current, params[:notes])
Query(Issue)

# Q 1639 : # @issue.init_journal
Query(Issue)

# Q 1640 : # User.current
Query(User)

# Q 1641 : # @project.wiki
Query(Wiki)
.where("id = ?")
# Q 1642 : # custom_values.each
Query(CustomValue)

# Q 1643 : # @project.active?
Query(Project)

# Q 1644 : # Role.find(:all, :order => "builtin, position")
Query(Role)
.where("id = ?")
# Q 1645 : # Role.find(:all, :order => "builtin, position")
Query(Role)
.where("id = ?")
# Q 1646 : # Role.find
Query(Role)
.where("id = ?")
# Q 1647 : # @changeset.changes.find(:all, :limit => @changes_pages.items_per_page, :offset => @changes_pages.current.offset)
Query(Change)
.where("changeset_id = ?")
.where("id = ?")
# Q 1648 : # @changeset.changes.find(:all, :limit => @changes_pages.items_per_page, :offset => @changes_pages.current.offset)
Query(Change)
.where("changeset_id = ?")
.where("id = ?")
# Q 1649 : # @changeset.changes.find
Query(Change)
.where("changeset_id = ?")
.where("id = ?")
# Q 1650 : # @changeset.changes
Query(Change)
.where("changeset_id = ?")
# Q 1651 : # user.update_attribute(:last_login_on, Time.now)
Query(User)

# Q 1652 : # user.update_attribute
Query(User)

# Q 1653 : # changes.find_by_path_and_revision(scm.with_leading_slash(revision.paths[0][:path]), revision.paths[0][:revision])
Query(Change)
.where("path = ?")
.where("revision = ?")
# Q 1654 : # changes.find_by_path_and_revision
Query(Change)
.where("path = ?")
.where("revision = ?")
# Q 1655 : # changes.find_by_path_and_revision(scm.with_leading_slash(revision.paths[0][:path]), revision.paths[0][:revision])
Query(Change)
.where("path = ?")
.where("revision = ?")
# Q 1656 : # changes.find_by_path_and_revision
Query(Change)
.where("path = ?")
.where("revision = ?")
# Q 1657 : # changes.find_by_path_and_revision(scm.with_leading_slash(revision.paths[0][:path]), revision.paths[0][:revision])
Query(Change)
.where("path = ?")
.where("revision = ?")
# Q 1658 : # changes.find_by_path_and_revision
Query(Change)
.where("path = ?")
.where("revision = ?")
# Q 1659 : # changes.find_by_path_and_revision(scm.with_leading_slash(revision.paths[0][:path]), revision.paths[0][:revision])
Query(Change)
.where("path = ?")
.where("revision = ?")
# Q 1660 : # changes.find_by_path_and_revision
Query(Change)
.where("path = ?")
.where("revision = ?")
# Q 1661 : # token.user.language
Query(User)
.where("id = ?")
.select('language')
# Q 1662 : # token.user
Query(User)
.where("id = ?")
# Q 1663 : # token.user.language
Query(User)
.where("id = ?")
.select('language')
# Q 1664 : # token.user
Query(User)
.where("id = ?")
# Q 1665 : # token.user.mail
Query(User)
.where("id = ?")
# Q 1666 : # token.user
Query(User)
.where("id = ?")
# Q 1667 : # token.user.mail
Query(User)
.where("id = ?")
# Q 1668 : # token.user
Query(User)
.where("id = ?")
# Q 1669 : # Attachment.create(:container => @issue, :file => file, :author => logged_in_user)
Query(Attachment)

# Q 1670 : # Attachment.create(:container => @issue, :file => file, :author => logged_in_user)
Query(Attachment)

# Q 1671 : # Attachment.create
Query(Attachment)

# Q 1672 : # JournalDetail.new(:property => "cf", :prop_key => c.custom_field_id, :old_value => @custom_values_before_change[c.custom_field_id], :value => c.value)
Query(JournalDetail)

# Q 1673 : # JournalDetail.new
Query(JournalDetail)

# Q 1674 : # changesets.find(:first, :conditions => { :committed_on => revision.time - time_delta..revision.time + time_delta, :committer => revision.author, :comments => revision.message })
Query(Changeset)
.where("id = ?")
# Q 1675 : # changesets.find(:first, :conditions => { :committed_on => revision.time - time_delta..revision.time + time_delta, :committer => revision.author, :comments => revision.message })
Query(Changeset)
.where("id = ?")
# Q 1676 : # changesets.find
Query(Changeset)
.where("id = ?")
# Q 1677 : # changesets.find(:first, :conditions => { :committed_on => revision.time - time_delta..revision.time + time_delta, :committer => revision.author, :comments => revision.message })
Query(Changeset)
.where("id = ?")
# Q 1678 : # changesets.find
Query(Changeset)
.where("id = ?")
# Q 1679 : # changesets.find(:first, :conditions => { :committed_on => revision.time - time_delta..revision.time + time_delta, :committer => revision.author, :comments => revision.message })
Query(Changeset)
.where("id = ?")
# Q 1680 : # changesets.find
Query(Changeset)
.where("id = ?")
# Q 1681 : # changesets.find(:first, :conditions => { :committed_on => revision.time - time_delta..revision.time + time_delta, :committer => revision.author, :comments => revision.message })
Query(Changeset)
.where("id = ?")
# Q 1682 : # changesets.find
Query(Changeset)
.where("id = ?")
# Q 1683 : # changesets.find(:first, :conditions => { :committed_on => revision.time - time_delta..revision.time + time_delta, :committer => revision.author, :comments => revision.message })
Query(Changeset)
.where("id = ?")
# Q 1684 : # changesets.find
Query(Changeset)
.where("id = ?")
# Q 1685 : # changesets.find(:first, :conditions => { :committed_on => revision.time - time_delta..revision.time + time_delta, :committer => revision.author, :comments => revision.message })
Query(Changeset)
.where("id = ?")
# Q 1686 : # changesets.find
Query(Changeset)
.where("id = ?")
# Q 1687 : # journal.details
Query(JournalDetail)
.where("journal_id = ?")
# Q 1688 : # JournalDetail.new(:property => "attachment", :prop_key => a.id, :value => a.filename)
Query(JournalDetail)

# Q 1689 : # JournalDetail.new
Query(JournalDetail)

# Q 1690 : # @roles.each
Query(Role)

# Q 1691 : # values_for(field).first
Query(Query)
.return_limit('1')
# Q 1692 : # values_for(field).first
Query(Query)
.return_limit('1')
# Q 1693 : # values_for(field).first
Query(Query)
.return_limit('1')
# Q 1694 : # role.id.to_s
Query(Role)

# Q 1695 : # role.id
Query(Role)

# Q 1696 : # role.id.to_s
Query(Role)

# Q 1697 : # role.id
Query(Role)

# Q 1698 : # members.any?
Query(Member)

# Q 1699 : # token.value
Query(Token)
.select('value')
# Q 1700 : # token.value
Query(Token)
.select('value')
# Q 1701 : # @project.is_public?
Query(Project)

# Q 1702 : # User.current.member_of?(@project)
Query(User)

# Q 1703 : # User.current.member_of?
Query(User)

# Q 1704 : # User.current
Query(User)

# Q 1705 : # User.current.admin?
Query(User)

# Q 1706 : # User.current
Query(User)

# Q 1707 : # @user.pref
Query(User)

# Q 1708 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 1709 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 1710 : # Project.find
Query(Project)
.where("id = ?")
# Q 1711 : # role.save
Query(Role)

# Q 1712 : # role.save
Query(Role)

# Q 1713 : # IssueCustomField.find(params[:custom_field_ids])
Query(IssueCustomField)
.where("id = ?")
# Q 1714 : # IssueCustomField.find(params[:custom_field_ids])
Query(IssueCustomField)
.where("id = ?")
# Q 1715 : # IssueCustomField.find
Query(IssueCustomField)
.where("id = ?")
# Q 1716 : # User.current.logged?
Query(User)

# Q 1717 : # User.current
Query(User)

# Q 1718 : # User.find(params[:id])
Query(User)
.where("id = ?")
# Q 1719 : # User.find(params[:id])
Query(User)
.where("id = ?")
# Q 1720 : # User.find
Query(User)
.where("id = ?")
# Q 1721 : # journal.save
Query(Journal)

# Q 1722 : # Member.find(params[:membership_id]).destroy
Query(Member)
.where("id = ?")
# Q 1723 : # Member.find(params[:membership_id])
Query(Member)
.where("id = ?")
# Q 1724 : # Member.find
Query(Member)
.where("id = ?")
# Q 1725 : # ProjectCustomField.find(:all).collect
Query(ProjectCustomField)
.where("id = ?")
# Q 1726 : # ProjectCustomField.find(:all)
Query(ProjectCustomField)
.where("id = ?")
# Q 1727 : # ProjectCustomField.find
Query(ProjectCustomField)
.where("id = ?")
# Q 1728 : # CustomValue.new(:custom_field => x, :customized => @project, :value => params["custom_fields"][x.id.to_s])
Query(CustomValue)

# Q 1729 : # CustomValue.new
Query(CustomValue)

# Q 1730 : # Setting.self_registration?
Query(Setting)

# Q 1731 : # user.language
Query(User)
.select('language')
# Q 1732 : # user.language
Query(User)
.select('language')
# Q 1733 : # Setting.notified_events.include?("issue_updated")
Query(Setting)

# Q 1734 : # Setting.notified_events.include?
Query(Setting)

# Q 1735 : # Setting.notified_events
Query(Setting)

# Q 1736 : # user.mail
Query(User)

# Q 1737 : # user.mail
Query(User)

# Q 1738 : # Token.find_by_action_and_value("register", params[:token])
Query(Token)
.where(" = ?")
.where("action = ?")
.where("value = ?")
# Q 1739 : # Token.find_by_action_and_value("register", params[:token])
Query(Token)
.where(" = ?")
.where("action = ?")
.where("value = ?")
# Q 1740 : # Token.find_by_action_and_value
Query(Token)
.where("action = ?")
.where("value = ?")
# Q 1741 : # token.expired?
Query(Token)

# Q 1742 : # @project.save
Query(Project)

# Q 1743 : # @repository.id
Query(Repository)

# Q 1744 : # self.user_id
Query(Query)
.select('user_id')
# Q 1745 : # user.id
Query(User)

# Q 1746 : # @wiki.find_page(params[:page])
Query(Wiki)

# Q 1747 : # @wiki.find_page(params[:page])
Query(Wiki)

# Q 1748 : # @wiki.find_page
Query(Wiki)

# Q 1749 : # token.user
Query(User)
.where("id = ?")
# Q 1750 : # token.user
Query(User)
.where("id = ?")
# Q 1751 : # user.allowed_to?(:manage_public_queries, project)
Query(User)

# Q 1752 : # user.allowed_to?
Query(User)

# Q 1753 : # changesets.minimum(:revision)
Query(Changeset)

# Q 1754 : # changesets.minimum(:revision)
Query(Changeset)

# Q 1755 : # changesets.minimum
Query(Changeset)

# Q 1756 : # changesets.minimum(:revision)
Query(Changeset)

# Q 1757 : # changesets.minimum
Query(Changeset)

# Q 1758 : # changesets.minimum(:revision)
Query(Changeset)

# Q 1759 : # changesets.minimum
Query(Changeset)

# Q 1760 : # changesets.minimum(:revision)
Query(Changeset)

# Q 1761 : # changesets.minimum
Query(Changeset)

# Q 1762 : # changesets.minimum(:revision)
Query(Changeset)

# Q 1763 : # changesets.minimum
Query(Changeset)

# Q 1764 : # changesets.minimum(:revision)
Query(Changeset)

# Q 1765 : # changesets.minimum
Query(Changeset)

# Q 1766 : # changesets.minimum(:revision)
Query(Changeset)

# Q 1767 : # changesets.minimum
Query(Changeset)

# Q 1768 : # changesets.minimum(:revision)
Query(Changeset)

# Q 1769 : # changesets.minimum
Query(Changeset)

# Q 1770 : # user.status
Query(User)
.select('status')
# Q 1771 : # @repository.diff(@path, @rev, @rev_to, @diff_type)
Query(Repository)

# Q 1772 : # @repository.diff(@path, @rev, @rev_to, @diff_type)
Query(Repository)

# Q 1773 : # @repository.diff
Query(Repository)

# Q 1774 : # self.status
Query(User)
.select('status')
# Q 1775 : # User.find(params[:id]).destroy
Query(User)
.where("id = ?")
# Q 1776 : # User.find(params[:id])
Query(User)
.where("id = ?")
# Q 1777 : # User.find
Query(User)
.where("id = ?")
# Q 1778 : # user.save
Query(User)

# Q 1779 : # token.destroy
Query(Token)

# Q 1780 : # Changeset.create(:repository => self, :revision => next_rev, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1781 : # Changeset.create(:repository => self, :revision => next_rev, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1782 : # Changeset.create
Query(Changeset)

# Q 1783 : # Changeset.create(:repository => self, :revision => next_rev, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1784 : # Changeset.create
Query(Changeset)

# Q 1785 : # Changeset.create(:repository => self, :revision => next_rev, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1786 : # Changeset.create
Query(Changeset)

# Q 1787 : # Changeset.create(:repository => self, :revision => next_rev, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1788 : # Changeset.create
Query(Changeset)

# Q 1789 : # Changeset.create(:repository => self, :revision => next_rev, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1790 : # Changeset.create
Query(Changeset)

# Q 1791 : # Changeset.create(:repository => self, :revision => next_rev, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1792 : # Changeset.create
Query(Changeset)

# Q 1793 : # Changeset.create(:repository => self, :revision => next_rev, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1794 : # Changeset.create
Query(Changeset)

# Q 1795 : # Changeset.create(:repository => self, :revision => next_rev, :committer => revision.author, :committed_on => revision.time, :comments => revision.message)
Query(Changeset)

# Q 1796 : # Changeset.create
Query(Changeset)

# Q 1797 : # @time_entry.user
Query(User)
.where("id = ?")
# Q 1798 : # @issue.status.find_new_statuses_allowed_to(logged_in_user.role_for_project(@project), @issue.tracker)
Query(IssueStatus)
.where("id = ?")
# Q 1799 : # @issue.status.find_new_statuses_allowed_to(logged_in_user.role_for_project(@project), @issue.tracker)
Query(IssueStatus)
.where("id = ?")
# Q 1800 : # @issue.status.find_new_statuses_allowed_to
Query(IssueStatus)
.where("id = ?")
# Q 1801 : # @issue.status
Query(IssueStatus)
.where("id = ?")
# Q 1802 : # @issue.tracker
Query(Tracker)
.where("id = ?")
# Q 1803 : # IssueStatus.find(:all, :order => "position").collect
Query(IssueStatus)
.where("id = ?")
# Q 1804 : # IssueStatus.find(:all, :order => "position")
Query(IssueStatus)
.where("id = ?")
# Q 1805 : # IssueStatus.find
Query(IssueStatus)
.where("id = ?")
# Q 1806 : # members.select { |m|
#   
#   m.role.assignable?
# }.collect
Query(Member)

# Q 1807 : # members.select
Query(Member)

# Q 1808 : # self.status
Query(User)
.select('status')
# Q 1809 : # Setting.default_language
Query(Setting)

# Q 1810 : # Setting.default_language
Query(Setting)

# Q 1811 : # TimeEntry.new(:project => @project, :issue => @issue, :user => logged_in_user, :spent_on => Date.today)
Query(TimeEntry)

# Q 1812 : # TimeEntry.new
Query(TimeEntry)

# Q 1813 : # IssueStatus.find(params[:new_status_id])
Query(IssueStatus)
.where("id = ?")
# Q 1814 : # IssueStatus.find(params[:new_status_id])
Query(IssueStatus)
.where("id = ?")
# Q 1815 : # IssueStatus.find
Query(IssueStatus)
.where("id = ?")
# Q 1816 : # self.closed?
Query(Issue)

# Q 1817 : # Tracker.find(:all, :order => "position").collect
Query(Tracker)
.where("id = ?")
# Q 1818 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 1819 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 1820 : # Setting.mail_from
Query(Setting)

# Q 1821 : # Setting.mail_from
Query(Setting)

# Q 1822 : # @wiki.find_page(params[:page])
Query(Wiki)

# Q 1823 : # @wiki.find_page(params[:page])
Query(Wiki)

# Q 1824 : # @wiki.find_page
Query(Wiki)

# Q 1825 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 1826 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 1827 : # Project.find
Query(Project)
.where("id = ?")
# Q 1828 : # Enumeration.find(:all, :conditions => ["opt=?", "IPRI"]).collect
Query(Enumeration)
.where("opt = ?")
.where("id = ?")
.where("id = ?")
# Q 1829 : # Enumeration.find(:all, :conditions => ["opt=?", "IPRI"])
Query(Enumeration)
.where("opt = ?")
.where("id = ?")
.where("id = ?")
# Q 1830 : # Enumeration.find
Query(Enumeration)
.where("id = ?")
# Q 1831 : # Setting.host_name
Query(Setting)

# Q 1832 : # Setting.host_name
Query(Setting)

# Q 1833 : # Setting.host_name
Query(Setting)

# Q 1834 : # Setting.host_name
Query(Setting)

# Q 1835 : # @time_entry.save
Query(TimeEntry)

# Q 1836 : # Setting.protocol
Query(Setting)

# Q 1837 : # Setting.protocol
Query(Setting)

# Q 1838 : # Setting.protocol
Query(Setting)

# Q 1839 : # Setting.protocol
Query(Setting)

# Q 1840 : # @issue.init_journal(self.logged_in_user, params[:notes])
Query(Issue)

# Q 1841 : # @issue.init_journal(self.logged_in_user, params[:notes])
Query(Issue)

# Q 1842 : # @issue.init_journal
Query(Issue)

# Q 1843 : # settings.is_a?(Hash)
Query(Setting)

# Q 1844 : # settings.is_a?
Query(Setting)

# Q 1845 : # self.status
Query(User)
.select('status')
# Q 1846 : # @time_entry.project
Query(Project)
.where("id = ?")
# Q 1847 : # @time_entry.issue
Query(Issue)
.where("id = ?")
# Q 1848 : # members.select { |m|
#   
#   m.mail_notification? || m.user.mail_notification?
# }.collect
Query(Member)

# Q 1849 : # members.select
Query(Member)

# Q 1850 : # @project.name
Query(Project)
.select('name')
# Q 1851 : # @issue.update_attributes(params[:issue])
Query(Issue)

# Q 1852 : # @issue.update_attributes
Query(Issue)

# Q 1853 : # User.new(:language => Setting.default_language)
Query(User)

# Q 1854 : # User.new(:language => Setting.default_language)
Query(User)

# Q 1855 : # User.new
Query(User)

# Q 1856 : # Setting.default_language
Query(Setting)

# Q 1857 : # UserCustomField.find(:all).collect
Query(UserCustomField)
.where("id = ?")
# Q 1858 : # UserCustomField.find(:all)
Query(UserCustomField)
.where("id = ?")
# Q 1859 : # UserCustomField.find
Query(UserCustomField)
.where("id = ?")
# Q 1860 : # CustomValue.new(:custom_field => x, :customized => @user)
Query(CustomValue)

# Q 1861 : # CustomValue.new
Query(CustomValue)

# Q 1862 : # self.status
Query(IssueStatus)
.where("id = ?")
# Q 1863 : # self.status
Query(IssueStatus)
.where("id = ?")
# Q 1864 : # Setting.app_title
Query(Setting)

# Q 1865 : # Enumeration::get_values("ACTI")
Query(Enumeration)

# Q 1866 : # Enumeration::get_values("ACTI")
Query(Enumeration)

# Q 1867 : # Enumeration::get_values
Query(Enumeration)

# Q 1868 : # User.hash_password(clear_password)
Query(User)

# Q 1869 : # User.hash_password
Query(User)

# Q 1870 : # self.hashed_password
Query(User)
.select('hashed_password')
# Q 1871 : # User.new(params[:user])
Query(User)

# Q 1872 : # User.new(params[:user])
Query(User)

# Q 1873 : # User.new
Query(User)

# Q 1874 : # Attachment.create(:container => @issue, :file => file, :author => logged_in_user)
Query(Attachment)

# Q 1875 : # Attachment.create(:container => @issue, :file => file, :author => logged_in_user)
Query(Attachment)

# Q 1876 : # Attachment.create
Query(Attachment)

# Q 1877 : # @project.active?
Query(Project)

# Q 1878 : # @project.archive
Query(Project)

# Q 1879 : # journal.details
Query(JournalDetail)
.where("journal_id = ?")
# Q 1880 : # JournalDetail.new(:property => "attachment", :prop_key => a.id, :value => a.filename)
Query(JournalDetail)

# Q 1881 : # JournalDetail.new
Query(JournalDetail)

# Q 1882 : # tracker.custom_fields
Query(IssueCustomField)
.where("id = ?")
# Q 1883 : # project.users.collect
Query(User)
.where("project_id = ?")
# Q 1884 : # project.users
Query(User)
.where("project_id = ?")
# Q 1885 : # UserPreference.new(:user => self)
Query(UserPreference)

# Q 1886 : # UserPreference.new
Query(UserPreference)

# Q 1887 : # self.custom_values.each
Query(CustomValue)
.where("issue_id = ?")
# Q 1888 : # self.custom_values
Query(CustomValue)
.where("issue_id = ?")
# Q 1889 : # custom_field.id
Query(CustomField)

# Q 1890 : # @wiki.pages
Query(WikiPage)
.where("wiki_id = ?")
# Q 1891 : # WikiPage.table_name
Query(WikiPage)

# Q 1892 : # WikiContent.table_name
Query(WikiContent)

# Q 1893 : # TimeEntry.find(params[:id])
Query(TimeEntry)
.where("id = ?")
# Q 1894 : # TimeEntry.find(params[:id])
Query(TimeEntry)
.where("id = ?")
# Q 1895 : # TimeEntry.find
Query(TimeEntry)
.where("id = ?")
# Q 1896 : # UserCustomField.find(:all).collect
Query(UserCustomField)
.where("id = ?")
# Q 1897 : # UserCustomField.find(:all)
Query(UserCustomField)
.where("id = ?")
# Q 1898 : # UserCustomField.find
Query(UserCustomField)
.where("id = ?")
# Q 1899 : # CustomValue.new(:custom_field => x, :customized => @user, :value => params["custom_fields"][x.id.to_s])
Query(CustomValue)

# Q 1900 : # CustomValue.new
Query(CustomValue)

# Q 1901 : # Issue.table_name
Query(Issue)

# Q 1902 : # IssueStatus.table_name
Query(IssueStatus)

# Q 1903 : # Tracker.table_name
Query(Tracker)

# Q 1904 : # WikiContent.table_name
Query(WikiContent)

# Q 1905 : # WikiContent.table_name
Query(WikiContent)

# Q 1906 : # WikiPage.table_name
Query(WikiPage)

# Q 1907 : # @time_entry.project
Query(Project)
.where("id = ?")
# Q 1908 : # @time_entry.project
Query(Project)
.where("id = ?")
# Q 1909 : # @project.active?
Query(Project)

# Q 1910 : # @project.unarchive
Query(Project)

# Q 1911 : # IssueCustomField.for_all
Query(IssueCustomField)

# Q 1912 : # Change.create(:changeset => cs, :action => action, :path => scm.with_leading_slash(revision.paths[0][:path]), :revision => revision.paths[0][:revision], :branch => revision.paths[0][:branch])
Query(Change)

# Q 1913 : # Change.create
Query(Change)

# Q 1914 : # Change.create(:changeset => cs, :action => action, :path => scm.with_leading_slash(revision.paths[0][:path]), :revision => revision.paths[0][:revision], :branch => revision.paths[0][:branch])
Query(Change)

# Q 1915 : # Change.create
Query(Change)

# Q 1916 : # Change.create(:changeset => cs, :action => action, :path => scm.with_leading_slash(revision.paths[0][:path]), :revision => revision.paths[0][:revision], :branch => revision.paths[0][:branch])
Query(Change)

# Q 1917 : # Change.create
Query(Change)

# Q 1918 : # Change.create(:changeset => cs, :action => action, :path => scm.with_leading_slash(revision.paths[0][:path]), :revision => revision.paths[0][:revision], :branch => revision.paths[0][:branch])
Query(Change)

# Q 1919 : # Change.create(:changeset => cs, :action => action, :path => scm.with_leading_slash(revision.paths[0][:path]), :revision => revision.paths[0][:revision], :branch => revision.paths[0][:branch])
Query(Change)

# Q 1920 : # Change.create
Query(Change)

# Q 1921 : # Change.create(:changeset => cs, :action => action, :path => scm.with_leading_slash(revision.paths[0][:path]), :revision => revision.paths[0][:revision], :branch => revision.paths[0][:branch])
Query(Change)

# Q 1922 : # Token.new(:user => @user, :action => "register")
Query(Token)

# Q 1923 : # Token.new(:user => @user, :action => "register")
Query(Token)

# Q 1924 : # Token.new
Query(Token)

# Q 1925 : # Issue.find(params[:issue_id])
Query(Issue)
.where("id = ?")
# Q 1926 : # Issue.find(params[:issue_id])
Query(Issue)
.where("id = ?")
# Q 1927 : # Issue.find
Query(Issue)
.where("id = ?")
# Q 1928 : # @user.save
Query(User)

# Q 1929 : # token.save
Query(Token)

# Q 1930 : # self.rss_token
Query(User)

# Q 1931 : # Token.create(:user => self, :action => "feeds")
Query(Token)

# Q 1932 : # Token.create
Query(Token)

# Q 1933 : # @issue.project
Query(Project)
.where("id = ?")
# Q 1934 : # @issue.project
Query(Project)
.where("id = ?")
# Q 1935 : # TimeEntry.new(:project => @project, :issue => @issue, :user => logged_in_user, :spent_on => Date.today)
Query(TimeEntry)

# Q 1936 : # TimeEntry.new
Query(TimeEntry)

# Q 1937 : # @project.id
Query(Project)

# Q 1938 : # Journal.new(:journalized => self, :user => user, :notes => notes)
Query(Journal)

# Q 1939 : # Journal.new
Query(Journal)

# Q 1940 : # token.value
Query(Token)
.select('value')
# Q 1941 : # self.clone
Query(Issue)

# Q 1942 : # self.clone
Query(Issue)

# Q 1943 : # project.name
Query(Project)
.select('name')
# Q 1944 : # @wiki.pages
Query(WikiPage)
.where("wiki_id = ?")
# Q 1945 : # Project.find(params[:project_id])
Query(Project)
.where("id = ?")
# Q 1946 : # Project.find(params[:project_id])
Query(Project)
.where("id = ?")
# Q 1947 : # Project.find
Query(Project)
.where("id = ?")
# Q 1948 : # @time_entry.save
Query(TimeEntry)

# Q 1949 : # self.custom_values.each
Query(CustomValue)
.where("issue_id = ?")
# Q 1950 : # self.custom_values
Query(CustomValue)
.where("issue_id = ?")
# Q 1951 : # Setting.app_title
Query(Setting)

# Q 1952 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 1953 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 1954 : # Project.find
Query(Project)
.where("id = ?")
# Q 1955 : # @project.issue_categories.collect
Query(IssueCategory)
.where("project_id = ?")
# Q 1956 : # @project.issue_categories
Query(IssueCategory)
.where("project_id = ?")
# Q 1957 : # Setting.notified_events.include?("issue_updated")
Query(Setting)

# Q 1958 : # Setting.notified_events.include?
Query(Setting)

# Q 1959 : # Setting.notified_events
Query(Setting)

# Q 1960 : # @project.versions.sort.collect
Query(Version)
.where("project_id = ?")
# Q 1961 : # @project.versions.sort
Query(Version)
.where("project_id = ?")
# Q 1962 : # @project.versions
Query(Version)
.where("project_id = ?")
# Q 1963 : # changesets.maximum(:revision)
Query(Changeset)

# Q 1964 : # changesets.maximum
Query(Changeset)

# Q 1965 : # @project.active_children.empty?
Query(Project)

# Q 1966 : # @project.active_children
Query(Project)

# Q 1967 : # changesets.find(:all, :conditions => ["revision < 0"], :order => "committed_on ASC").each()
Query(Changeset)
.where("revision = ?")
.where("id = ?")
.where("id = ?")
# Q 1968 : # changesets.find(:all, :conditions => ["revision < 0"], :order => "committed_on ASC").each
Query(Changeset)
.where("revision = ?")
.where("id = ?")
.where("id = ?")
# Q 1969 : # changesets.find(:all, :conditions => ["revision < 0"], :order => "committed_on ASC")
Query(Changeset)
.where("revision = ?")
.where("id = ?")
.where("id = ?")
# Q 1970 : # changesets.find
Query(Changeset)
.where("id = ?")
# Q 1971 : # changesets.find(:all, :conditions => ["revision < 0"], :order => "committed_on ASC").each()
Query(Changeset)
.where("revision = ?")
.where("id = ?")
.where("id = ?")
# Q 1972 : # changesets.find(:all, :conditions => ["revision < 0"], :order => "committed_on ASC").each
Query(Changeset)
.where("revision = ?")
.where("id = ?")
.where("id = ?")
# Q 1973 : # changesets.find(:all, :conditions => ["revision < 0"], :order => "committed_on ASC")
Query(Changeset)
.where("revision = ?")
.where("id = ?")
.where("id = ?")
# Q 1974 : # changesets.find
Query(Changeset)
.where("id = ?")
# Q 1975 : # @project.active_children.collect
Query(Project)

# Q 1976 : # @project.active_children
Query(Project)

# Q 1977 : # self.status.is_closed?
Query(IssueStatus)
.where("id = ?")
# Q 1978 : # self.status
Query(IssueStatus)
.where("id = ?")
# Q 1979 : # Member.update_all("mail_notification = #{
# connection.quoted_false}", ["user_id = ?", id])
Query(Member)

# Q 1980 : # Member.update_all
Query(Member)

# Q 1981 : # user.is_a?(User)
Query(User)

# Q 1982 : # user.is_a?
Query(User)

# Q 1983 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 1984 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 1985 : # Project.find
Query(Project)
.where("id = ?")
# Q 1986 : # @project.all_custom_fields.select(&:is_filter?).each
Query(Project)
.select('is_filter?')
# Q 1987 : # @project.all_custom_fields.select(&:is_filter?)
Query(Project)
.select('is_filter?')
# Q 1988 : # @project.all_custom_fields.select
Query(Project)

# Q 1989 : # @project.all_custom_fields
Query(Project)

# Q 1990 : # Member.update_all("mail_notification = #{
# connection.quoted_true}", ["user_id = ? AND project_id IN (?)", id, ids])
Query(Member)

# Q 1991 : # Member.update_all
Query(Member)

# Q 1992 : # changeset.save!
Query(Changeset)

# Q 1993 : # changeset.save!
Query(Changeset)

# Q 1994 : # changeset.save!
Query(Changeset)

# Q 1995 : # changeset.save!
Query(Changeset)

# Q 1996 : # Issue.table_name
Query(Issue)

# Q 1997 : # IssueStatus.table_name
Query(IssueStatus)

# Q 1998 : # Version.table_name
Query(Version)

# Q 1999 : # @project.repository
Query(Repository)
.where("id = ?")
# Q 2000 : # @project.repository
Query(Repository)
.where("id = ?")
# Q 2001 : # user.id
Query(User)

# Q 2002 : # user.id
Query(User)

# Q 2003 : # @wiki.find_page(params[:page])
Query(Wiki)

# Q 2004 : # @wiki.find_page(params[:page])
Query(Wiki)

# Q 2005 : # @wiki.find_page
Query(Wiki)

# Q 2006 : # @project.members.find(:all, :include => :user).collect
Query(Member)
.where("project_id = ?")
.where("id = ?")
# Q 2007 : # @project.members.find(:all, :include => :user)
Query(Member)
.where("project_id = ?")
.where("id = ?")
# Q 2008 : # @project.members.find
Query(Member)
.where("project_id = ?")
.where("id = ?")
# Q 2009 : # @project.members
Query(Member)
.where("project_id = ?")
# Q 2010 : # User.anonymous
Query(User)

# Q 2011 : # User.anonymous
Query(User)

# Q 2012 : # @project.issue_categories.build(params[:category])
Query(IssueCategory)
.where("project_id = ?")
# Q 2013 : # @project.issue_categories.build(params[:category])
Query(IssueCategory)
.where("project_id = ?")
# Q 2014 : # @project.issue_categories.build
Query(IssueCategory)
.where("project_id = ?")
# Q 2015 : # @project.issue_categories
Query(IssueCategory)
.where("project_id = ?")
# Q 2016 : # project.assignable_users
Query(Project)

# Q 2017 : # Enumeration::get_values("ACTI")
Query(Enumeration)

# Q 2018 : # Enumeration::get_values("ACTI")
Query(Enumeration)

# Q 2019 : # Enumeration::get_values
Query(Enumeration)

# Q 2020 : # @project.id
Query(Project)

# Q 2021 : # attachments.detect
Query(Attachment)

# Q 2022 : # attachments.detect
Query(Attachment)

# Q 2023 : # Token.find_by_value(key)
Query(Token)

# Q 2024 : # Token.find_by_value(key)
Query(Token)

# Q 2025 : # Token.find_by_value
Query(Token)

# Q 2026 : # token.user.active?
Query(User)
.where("id = ?")
# Q 2027 : # token.user
Query(User)
.where("id = ?")
# Q 2028 : # token.user
Query(User)
.where("id = ?")
# Q 2029 : # @issue.destroy
Query(Issue)

# Q 2030 : # @user.pref
Query(User)

# Q 2031 : # project.recipients
Query(Project)

# Q 2032 : # project.recipients
Query(Project)

# Q 2033 : # @user.pref.save
Query(User)

# Q 2034 : # @user.pref
Query(User)

# Q 2035 : # @wiki.find_page(params[:page])
Query(Wiki)

# Q 2036 : # @wiki.find_page(params[:page])
Query(Wiki)

# Q 2037 : # @wiki.find_page
Query(Wiki)

# Q 2038 : # Token.find_by_action_and_value("autologin", key)
Query(Token)
.where(" = ?")
.where("action = ?")
.where("value = ?")
# Q 2039 : # Token.find_by_action_and_value("autologin", key)
Query(Token)
.where(" = ?")
.where("action = ?")
.where("value = ?")
# Q 2040 : # Token.find_by_action_and_value
Query(Token)
.where("action = ?")
.where("value = ?")
# Q 2041 : # token.created_on
Query(Token)
.select('created_on')
# Q 2042 : # Setting.autologin.to_i.day.ago
Query(Setting)

# Q 2043 : # Setting.autologin.to_i.day
Query(Setting)

# Q 2044 : # Setting.autologin.to_i
Query(Setting)

# Q 2045 : # Setting.autologin
Query(Setting)

# Q 2046 : # token.user.active?
Query(User)
.where("id = ?")
# Q 2047 : # token.user
Query(User)
.where("id = ?")
# Q 2048 : # token.user
Query(User)
.where("id = ?")
# Q 2049 : # @issue.attachments.find(params[:attachment_id])
Query(Attachment)
.where("issue_id = ?")
.where("id = ?")
# Q 2050 : # @issue.attachments.find(params[:attachment_id])
Query(Attachment)
.where("issue_id = ?")
.where("id = ?")
# Q 2051 : # @issue.attachments.find
Query(Attachment)
.where("issue_id = ?")
.where("id = ?")
# Q 2052 : # @issue.attachments
Query(Attachment)
.where("issue_id = ?")
# Q 2053 : # @project.issue_categories
Query(IssueCategory)
.where("project_id = ?")
# Q 2054 : # @project.issue_categories
Query(IssueCategory)
.where("project_id = ?")
# Q 2055 : # @project.issue_categories
Query(IssueCategory)
.where("project_id = ?")
# Q 2056 : # @project.issue_categories
Query(IssueCategory)
.where("project_id = ?")
# Q 2057 : # @project.issue_categories
Query(IssueCategory)
.where("project_id = ?")
# Q 2058 : # Setting.text_formatting
Query(Setting)

# Q 2059 : # Attachment.create(:container => @page, :file => file, :author => logged_in_user)
Query(Attachment)

# Q 2060 : # Attachment.create(:container => @page, :file => file, :author => logged_in_user)
Query(Attachment)

# Q 2061 : # Attachment.create
Query(Attachment)

# Q 2062 : # @issue.init_journal(self.logged_in_user)
Query(Issue)

# Q 2063 : # @issue.init_journal(self.logged_in_user)
Query(Issue)

# Q 2064 : # @issue.init_journal
Query(Issue)

# Q 2065 : # Issue.table_name
Query(Issue)

# Q 2066 : # IssueStatus.table_name
Query(IssueStatus)

# Q 2067 : # Enumeration.table_name
Query(Enumeration)

# Q 2068 : # user.lastname
Query(User)
.select('lastname')
# Q 2069 : # user.firstname
Query(User)
.select('firstname')
# Q 2070 : # user.lastname
Query(User)
.select('lastname')
# Q 2071 : # journal.details
Query(JournalDetail)
.where("journal_id = ?")
# Q 2072 : # JournalDetail.new(:property => "attachment", :prop_key => a.id, :old_value => a.filename)
Query(JournalDetail)

# Q 2073 : # JournalDetail.new
Query(JournalDetail)

# Q 2074 : # time_entries.sum(:hours)
Query(TimeEntry)

# Q 2075 : # time_entries.sum
Query(TimeEntry)

# Q 2076 : # repository.changesets.count(:all, :group => :commit_date, :conditions => ["commit_date BETWEEN ? AND ?", @date_from, @date_to])
Query(Changeset)
.where("repository_id = ?")
# Q 2077 : # repository.changesets.count(:all, :group => :commit_date, :conditions => ["commit_date BETWEEN ? AND ?", @date_from, @date_to])
Query(Changeset)
.where("repository_id = ?")
# Q 2078 : # repository.changesets.count
Query(Changeset)
.where("repository_id = ?")
# Q 2079 : # repository.changesets
Query(Changeset)
.where("repository_id = ?")
# Q 2080 : # journal.save
Query(Journal)

# Q 2081 : # @project.id
Query(Project)

# Q 2082 : # @wiki.find_page(params[:page])
Query(Wiki)

# Q 2083 : # @wiki.find_page(params[:page])
Query(Wiki)

# Q 2084 : # @wiki.find_page
Query(Wiki)

# Q 2085 : # @project.versions.build(params[:version])
Query(Version)
.where("project_id = ?")
# Q 2086 : # @project.versions.build(params[:version])
Query(Version)
.where("project_id = ?")
# Q 2087 : # @project.versions.build
Query(Version)
.where("project_id = ?")
# Q 2088 : # @project.versions
Query(Version)
.where("project_id = ?")
# Q 2089 : # repository.changes.count(:all, :group => :commit_date, :conditions => ["commit_date BETWEEN ? AND ?", @date_from, @date_to])
Query(Change)
.where("repository_id = ?")
# Q 2090 : # repository.changes.count(:all, :group => :commit_date, :conditions => ["commit_date BETWEEN ? AND ?", @date_from, @date_to])
Query(Change)
.where("repository_id = ?")
# Q 2091 : # repository.changes.count
Query(Change)
.where("repository_id = ?")
# Q 2092 : # repository.changes
Query(Change)
.where("repository_id = ?")
# Q 2093 : # @version.save
Query(Version)

# Q 2094 : # Enumeration.get_values("IPRI").reverse
Query(Enumeration)

# Q 2095 : # Enumeration.get_values("IPRI").reverse
Query(Enumeration)

# Q 2096 : # Enumeration.get_values("IPRI")
Query(Enumeration)

# Q 2097 : # Enumeration.get_values
Query(Enumeration)

# Q 2098 : # IssueStatus.find(:all, :order => "position")
Query(IssueStatus)
.where("id = ?")
# Q 2099 : # IssueStatus.find(:all, :order => "position")
Query(IssueStatus)
.where("id = ?")
# Q 2100 : # IssueStatus.find
Query(IssueStatus)
.where("id = ?")
# Q 2101 : # @issue.status.find_new_statuses_allowed_to(User.current.role_for_project(@project), @issue.tracker)
Query(IssueStatus)
.where("id = ?")
# Q 2102 : # @issue.status.find_new_statuses_allowed_to(User.current.role_for_project(@project), @issue.tracker)
Query(IssueStatus)
.where("id = ?")
# Q 2103 : # @issue.status.find_new_statuses_allowed_to
Query(IssueStatus)
.where("id = ?")
# Q 2104 : # @issue.status
Query(IssueStatus)
.where("id = ?")
# Q 2105 : # User.current.role_for_project(@project)
Query(User)

# Q 2106 : # User.current.role_for_project
Query(User)

# Q 2107 : # User.current
Query(User)

# Q 2108 : # @issue.tracker
Query(Tracker)
.where("id = ?")
# Q 2109 : # @issue.assignable_users
Query(Issue)

# Q 2110 : # @issue.assignable_users
Query(Issue)

# Q 2111 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 2112 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 2113 : # Project.find
Query(Project)
.where("id = ?")
# Q 2114 : # @issue.assigned_to
Query(User)
.where("id = ?")
# Q 2115 : # @issue.assigned_to
Query(User)
.where("id = ?")
# Q 2116 : # @issue.assigned_to
Query(User)
.where("id = ?")
# Q 2117 : # @project.wiki
Query(Wiki)
.where("id = ?")
# Q 2118 : # @project.wiki
Query(Wiki)
.where("id = ?")
# Q 2119 : # User.current.allowed_to?(:edit_issues, @project)
Query(User)

# Q 2120 : # User.current.allowed_to?
Query(User)

# Q 2121 : # User.current
Query(User)

# Q 2122 : # project.active?
Query(Project)

# Q 2123 : # User.current.allowed_to?(:change_issue_status, @project)
Query(User)

# Q 2124 : # User.current.allowed_to?
Query(User)

# Q 2125 : # User.current
Query(User)

# Q 2126 : # Issue.table_name
Query(Issue)

# Q 2127 : # IssueStatus.table_name
Query(IssueStatus)

# Q 2128 : # IssueCategory.table_name
Query(IssueCategory)

# Q 2129 : # User.current.allowed_to?(:add_issues, @project)
Query(User)

# Q 2130 : # User.current.allowed_to?
Query(User)

# Q 2131 : # User.current
Query(User)

# Q 2132 : # @project.documents.build(params[:document])
Query(Document)
.where("project_id = ?")
# Q 2133 : # @project.documents.build(params[:document])
Query(Document)
.where("project_id = ?")
# Q 2134 : # @project.documents.build
Query(Document)
.where("project_id = ?")
# Q 2135 : # @project.documents
Query(Document)
.where("project_id = ?")
# Q 2136 : # project.id
Query(Project)

# Q 2137 : # User.current.allowed_to?(:move_issues, @project)
Query(User)

# Q 2138 : # User.current.allowed_to?
Query(User)

# Q 2139 : # User.current
Query(User)

# Q 2140 : # @document.save
Query(Document)

# Q 2141 : # User.current.allowed_to?(:delete_issues, @project)
Query(User)

# Q 2142 : # User.current.allowed_to?
Query(User)

# Q 2143 : # User.current
Query(User)

# Q 2144 : # @project.id
Query(Project)

# Q 2145 : # Attachment.create(:container => @document, :file => a, :author => logged_in_user)
Query(Attachment)

# Q 2146 : # Attachment.create
Query(Attachment)

# Q 2147 : # Role.non_member
Query(Role)

# Q 2148 : # Role.anonymous
Query(Role)

# Q 2149 : # Issue.find_by_id(params[:id])
Query(Issue)

# Q 2150 : # Issue.find_by_id(params[:id])
Query(Issue)

# Q 2151 : # Issue.find_by_id
Query(Issue)

# Q 2152 : # Setting.notified_events.include?("document_added")
Query(Setting)

# Q 2153 : # Setting.notified_events.include?
Query(Setting)

# Q 2154 : # Setting.notified_events
Query(Setting)

# Q 2155 : # issue.attachments
Query(Attachment)
.where("issue_id = ?")
# Q 2156 : # issue.attachments
Query(Attachment)
.where("issue_id = ?")
# Q 2157 : # Project.find_by_name($1)
Query(Project)

# Q 2158 : # Project.find_by_name
Query(Project)

# Q 2159 : # Project.find_by_identifier($1)
Query(Project)

# Q 2160 : # Project.find_by_identifier
Query(Project)

# Q 2161 : # Project.find_by_name($1)
Query(Project)

# Q 2162 : # Project.find_by_name
Query(Project)

# Q 2163 : # Project.find_by_identifier($1)
Query(Project)

# Q 2164 : # Project.find_by_identifier
Query(Project)

# Q 2165 : # Project.find_by_name($1)
Query(Project)

# Q 2166 : # Project.find_by_name
Query(Project)

# Q 2167 : # Project.find_by_identifier($1)
Query(Project)

# Q 2168 : # Project.find_by_identifier
Query(Project)

# Q 2169 : # Issue.table_name
Query(Issue)

# Q 2170 : # IssueStatus.table_name
Query(IssueStatus)

# Q 2171 : # User.table_name
Query(User)

# Q 2172 : # Issue.find(params[:id], :include => [:project, :tracker, :status, :author, :priority, :category])
Query(Issue)
.where("id = ?")
# Q 2173 : # Issue.find(params[:id], :include => [:project, :tracker, :status, :author, :priority, :category])
Query(Issue)
.where("id = ?")
# Q 2174 : # Issue.find
Query(Issue)
.where("id = ?")
# Q 2175 : # @project.documents
Query(Document)
.where("project_id = ?")
# Q 2176 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 2177 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 2178 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 2179 : # @issue.project
Query(Project)
.where("id = ?")
# Q 2180 : # @issue.project
Query(Project)
.where("id = ?")
# Q 2181 : # @project.id
Query(Project)

# Q 2182 : # documents.group_by
Query(Document)

# Q 2183 : # documents.group_by
Query(Document)

# Q 2184 : # project.active?
Query(Project)

# Q 2185 : # Wiki.titleize(page)
Query(Wiki)

# Q 2186 : # Wiki.titleize
Query(Wiki)

# Q 2187 : # Wiki.titleize(page)
Query(Wiki)

# Q 2188 : # Wiki.titleize
Query(Wiki)

# Q 2189 : # documents.select { |d|
#   
#   d.attachments.any?
# }.group_by
Query(Document)

# Q 2190 : # documents.select
Query(Document)

# Q 2191 : # project.allows_to?(action)
Query(Project)

# Q 2192 : # project.allows_to?
Query(Project)

# Q 2193 : # documents.group_by(&:category)
Query(Document)

# Q 2194 : # documents.group_by(&:category)
Query(Document)

# Q 2195 : # documents.group_by
Query(Document)

# Q 2196 : # Query.new(:name => "_", :executed_by => logged_in_user)
Query(Query)

# Q 2197 : # Query.new(:name => "_", :executed_by => logged_in_user)
Query(Query)

# Q 2198 : # Query.new
Query(Query)

# Q 2199 : # repository.changesets.count(:all, :group => :committer)
Query(Changeset)
.where("repository_id = ?")
# Q 2200 : # repository.changesets.count(:all, :group => :committer)
Query(Changeset)
.where("repository_id = ?")
# Q 2201 : # repository.changesets.count
Query(Changeset)
.where("repository_id = ?")
# Q 2202 : # repository.changesets
Query(Changeset)
.where("repository_id = ?")
# Q 2203 : # @query.add_filter(field, params[:operators][field], params[:values][field])
Query(Query)

# Q 2204 : # @query.add_filter
Query(Query)

# Q 2205 : # @query.add_filter(field, params[:operators][field], params[:values][field])
Query(Query)

# Q 2206 : # repository.changes.count(:all, :group => :committer)
Query(Change)
.where("repository_id = ?")
# Q 2207 : # repository.changes.count(:all, :group => :committer)
Query(Change)
.where("repository_id = ?")
# Q 2208 : # repository.changes.count
Query(Change)
.where("repository_id = ?")
# Q 2209 : # repository.changes
Query(Change)
.where("repository_id = ?")
# Q 2210 : # Query.available_columns
Query(Query)

# Q 2211 : # Query.available_columns
Query(Query)

# Q 2212 : # Issue.table_name
Query(Issue)

# Q 2213 : # IssueStatus.table_name
Query(IssueStatus)

# Q 2214 : # role.allowed_to?(action)
Query(Role)

# Q 2215 : # role.allowed_to?
Query(Role)

# Q 2216 : # project.is_public?
Query(Project)

# Q 2217 : # role.member?
Query(Role)

# Q 2218 : # @query.available_filters.keys.each
Query(Query)

# Q 2219 : # @query.available_filters.keys
Query(Query)

# Q 2220 : # @query.available_filters
Query(Query)

# Q 2221 : # @query.add_short_filter(field, params[field])
Query(Query)

# Q 2222 : # @query.add_short_filter
Query(Query)

# Q 2223 : # @query.add_short_filter(field, params[field])
Query(Query)

# Q 2224 : # @query.add_short_filter
Query(Query)

# Q 2225 : # @project.active_children.collect { |p|
#   
#   p.id
# }.join
Query(Project)

# Q 2226 : # @project.active_children.collect
Query(Project)

# Q 2227 : # @project.active_children
Query(Project)

# Q 2228 : # Issue.new.copy_from(params[:copy_from])
Query(Issue)

# Q 2229 : # Issue.new.copy_from
Query(Issue)

# Q 2230 : # Issue.new
Query(Issue)

# Q 2231 : # Issue.new(params[:issue])
Query(Issue)

# Q 2232 : # Issue.new
Query(Issue)

# Q 2233 : # @project.active_children.any?
Query(Project)

# Q 2234 : # @project.active_children
Query(Project)

# Q 2235 : # Setting.issue_list_default_columns.include?(c.name.to_s)
Query(Setting)

# Q 2236 : # Setting.issue_list_default_columns.include?
Query(Setting)

# Q 2237 : # Setting.issue_list_default_columns
Query(Setting)

# Q 2238 : # User.current
Query(User)

# Q 2239 : # User.current
Query(User)

# Q 2240 : # Tracker.find(params[:tracker_id])
Query(Tracker)
.where("id = ?")
# Q 2241 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 2242 : # IssueStatus.default
Query(IssueStatus)

# Q 2243 : # IssueStatus.default
Query(IssueStatus)

# Q 2244 : # project.changesets.find_by_revision(oid)
Query(Project)

# Q 2245 : # project.changesets.find_by_revision(oid)
Query(Project)

# Q 2246 : # project.changesets.find_by_revision
Query(Project)

# Q 2247 : # project.changesets
Query(Project)

# Q 2248 : # project.changesets.find_by_revision(oid)
Query(Project)

# Q 2249 : # project.changesets.find_by_revision
Query(Project)

# Q 2250 : # project.changesets
Query(Project)

# Q 2251 : # project.changesets.find_by_revision(oid)
Query(Project)

# Q 2252 : # project.changesets.find_by_revision
Query(Project)

# Q 2253 : # project.changesets
Query(Project)

# Q 2254 : # project.changesets.find_by_revision(oid)
Query(Project)

# Q 2255 : # project.changesets.find_by_revision
Query(Project)

# Q 2256 : # project.changesets
Query(Project)

# Q 2257 : # project.id
Query(Project)

# Q 2258 : # project.id
Query(Project)

# Q 2259 : # project.id
Query(Project)

# Q 2260 : # project.id
Query(Project)

# Q 2261 : # changeset.comments
Query(Changeset)
.select('comments')
# Q 2262 : # changeset.comments
Query(Changeset)
.select('comments')
# Q 2263 : # changeset.comments
Query(Changeset)
.select('comments')
# Q 2264 : # changeset.comments
Query(Changeset)
.select('comments')
# Q 2265 : # Issue.find_by_id(oid.to_i, :include => [:project, :status], :conditions => Project.visible_by(User.current))
Query(Issue)

# Q 2266 : # Issue.find_by_id(oid.to_i, :include => [:project, :status], :conditions => Project.visible_by(User.current))
Query(Issue)

# Q 2267 : # Issue.find_by_id
Query(Issue)

# Q 2268 : # Project.visible_by(User.current)
Query(Project)

# Q 2269 : # Project.visible_by
Query(Project)

# Q 2270 : # User.current
Query(User)

# Q 2271 : # Issue.find_by_id(oid.to_i, :include => [:project, :status], :conditions => Project.visible_by(User.current))
Query(Issue)

# Q 2272 : # Issue.find_by_id
Query(Issue)

# Q 2273 : # Project.visible_by(User.current)
Query(Project)

# Q 2274 : # Project.visible_by
Query(Project)

# Q 2275 : # User.current
Query(User)

# Q 2276 : # Issue.find_by_id(oid.to_i, :include => [:project, :status], :conditions => Project.visible_by(User.current))
Query(Issue)

# Q 2277 : # Issue.find_by_id
Query(Issue)

# Q 2278 : # Project.visible_by(User.current)
Query(Project)

# Q 2279 : # Project.visible_by
Query(Project)

# Q 2280 : # User.current
Query(User)

# Q 2281 : # @issue.tracker
Query(Tracker)
.where("id = ?")
# Q 2282 : # issue.subject
Query(Issue)
.select('subject')
# Q 2283 : # issue.status.name
Query(IssueStatus)
.where("id = ?")
.select('name')
# Q 2284 : # issue.status
Query(IssueStatus)
.where("id = ?")
# Q 2285 : # issue.subject
Query(Issue)
.select('subject')
# Q 2286 : # issue.status.name
Query(IssueStatus)
.where("id = ?")
.select('name')
# Q 2287 : # issue.status
Query(IssueStatus)
.where("id = ?")
# Q 2288 : # issue.subject
Query(Issue)
.select('subject')
# Q 2289 : # issue.status.name
Query(IssueStatus)
.where("id = ?")
.select('name')
# Q 2290 : # issue.status
Query(IssueStatus)
.where("id = ?")
# Q 2291 : # issue.subject
Query(Issue)
.select('subject')
# Q 2292 : # issue.status.name
Query(IssueStatus)
.where("id = ?")
.select('name')
# Q 2293 : # issue.status
Query(IssueStatus)
.where("id = ?")
# Q 2294 : # issue.status.name
Query(IssueStatus)
.where("id = ?")
.select('name')
# Q 2295 : # issue.closed?
Query(Issue)

# Q 2296 : # issue.closed?
Query(Issue)

# Q 2297 : # issue.closed?
Query(Issue)

# Q 2298 : # link = content_tag("del", link) if issue.closed?
Query(Issue)

# Q 2299 : # @issue.custom_values.empty?
Query(CustomValue)
.where("issue_id = ?")
# Q 2300 : # @issue.custom_values
Query(CustomValue)
.where("issue_id = ?")
# Q 2301 : # @project.custom_fields_for_issues(@issue.tracker).collect
Query(Project)

# Q 2302 : # @project.custom_fields_for_issues(@issue.tracker)
Query(Project)

# Q 2303 : # @project.custom_fields_for_issues
Query(Project)

# Q 2304 : # @issue.tracker
Query(Tracker)
.where("id = ?")
# Q 2305 : # CustomValue.new(:custom_field => x, :customized => @issue)
Query(CustomValue)

# Q 2306 : # CustomValue.new
Query(CustomValue)

# Q 2307 : # @issue.custom_values
Query(CustomValue)
.where("issue_id = ?")
# Q 2308 : # IssueStatus.find_by_id(params[:issue][:status_id])
Query(IssueStatus)

# Q 2309 : # IssueStatus.find_by_id(params[:issue][:status_id])
Query(IssueStatus)

# Q 2310 : # IssueStatus.find_by_id
Query(IssueStatus)

# Q 2311 : # @project.custom_fields_for_issues(@issue.tracker).collect
Query(Project)

# Q 2312 : # @project.custom_fields_for_issues(@issue.tracker)
Query(Project)

# Q 2313 : # @project.custom_fields_for_issues
Query(Project)

# Q 2314 : # @issue.tracker
Query(Tracker)
.where("id = ?")
# Q 2315 : # CustomValue.new(:custom_field => x, :customized => @issue, :value => params["custom_fields"][x.id.to_s])
Query(CustomValue)

# Q 2316 : # CustomValue.new
Query(CustomValue)

# Q 2317 : # @issue.save
Query(Issue)

# Q 2318 : # Attachment.create(:container => @issue, :file => a, :author => User.current)
Query(Attachment)

# Q 2319 : # Attachment.create
Query(Attachment)

# Q 2320 : # User.current
Query(User)

# Q 2321 : # project.active_children.collect
Query(Project)

# Q 2322 : # project.active_children
Query(Project)

# Q 2323 : # Setting.notified_events.include?("issue_added")
Query(Setting)

# Q 2324 : # Setting.notified_events.include?
Query(Setting)

# Q 2325 : # Setting.notified_events
Query(Setting)

# Q 2326 : # Issue.table_name
Query(Issue)

# Q 2327 : # project.id
Query(Project)

# Q 2328 : # Issue.table_name
Query(Issue)

# Q 2329 : # project.id
Query(Project)

# Q 2330 : # Enumeration::get_values("IPRI")
Query(Enumeration)

# Q 2331 : # Enumeration::get_values("IPRI")
Query(Enumeration)

# Q 2332 : # Enumeration::get_values
Query(Enumeration)

# Q 2333 : # Project.visible_by(executed_by)
Query(Project)

# Q 2334 : # Project.visible_by
Query(Project)

# Q 2335 : # Issue.table_name
Query(Issue)

# Q 2336 : # CustomValue.table_name
Query(CustomValue)

# Q 2337 : # CustomValue.table_name
Query(CustomValue)

# Q 2338 : # CustomValue.table_name
Query(CustomValue)

# Q 2339 : # db_table = CustomValue.table_name
Query(CustomValue)

# Q 2340 : # Issue.table_name
Query(Issue)

# Q 2341 : # Issue.table_name
Query(Issue)

# Q 2342 : # Issue.table_name
Query(Issue)

# Q 2343 : # Issue.table_name
Query(Issue)

# Q 2344 : # Issue.table_name
Query(Issue)

# Q 2345 : # Issue.table_name
Query(Issue)

# Q 2346 : # Issue.table_name
Query(Issue)

# Q 2347 : # Issue.table_name
Query(Issue)

# Q 2348 : # @query.valid?
Query(Query)

# Q 2349 : # Issue.table_name
Query(Issue)

# Q 2350 : # Issue.table_name
Query(Issue)

# Q 2351 : # Issue.table_name
Query(Issue)

# Q 2352 : # db_table = Issue.table_name
Query(Issue)

# Q 2353 : # Issue.count(:include => [:status, :project], :conditions => @query.statement)
Query(Issue)

# Q 2354 : # Issue.count(:include => [:status, :project], :conditions => @query.statement)
Query(Issue)

# Q 2355 : # Issue.count
Query(Issue)

# Q 2356 : # @query.statement
Query(Query)

# Q 2357 : # @query.statement
Query(Query)

# Q 2358 : # Issue.table_name
Query(Issue)

# Q 2359 : # @query.valid?
Query(Query)

# Q 2360 : # @query.statement
Query(Query)

# Q 2361 : # Setting.issues_export_limit.to_i
Query(Setting)

# Q 2362 : # Setting.issues_export_limit
Query(Setting)

# Q 2363 : # IssueStatus.table_name
Query(IssueStatus)

# Q 2364 : # IssueStatus.table_name
Query(IssueStatus)

# Q 2365 : # IssueStatus.table_name
Query(IssueStatus)

# Q 2366 : # IssueStatus.table_name
Query(IssueStatus)

# Q 2367 : # IssueStatus.table_name
Query(IssueStatus)

# Q 2368 : # IssueStatus.table_name
Query(IssueStatus)

# Q 2369 : # IssueStatus.table_name
Query(IssueStatus)

# Q 2370 : # IssueStatus.table_name
Query(IssueStatus)

# Q 2371 : # @project.all_custom_fields
Query(Project)

# Q 2372 : # custom_field.name
Query(CustomField)
.select('name')
# Q 2373 : # headers << custom_field.name
Query(CustomField)

# Q 2374 : # @issues.each
Query(Issue)

# Q 2375 : # @issues.each do |issue|
#   
#   fields = [issue.id, issue.status.name, issue.project.name, issue.tracker.name, issue.priority.name, issue.subject, (
#   issue.assigned_to ? issue.assigned_to.name : ""), issue.author.name, issue.start_date ? l_date(issue.start_date) : nil, issue.due_date ? l_date(issue.due_date) : nil, issue.done_ratio, l_datetime(issue.created_on), l_datetime(issue.updated_on)]
#   for custom_field in @project.all_custom_fields
#     
#     fields << (
#     show_value issue.custom_value_for(custom_field))
#   end
#   csv << fields.collect { |c|
#     
#     begin
#       
#       
#       ic.iconv(c.to_s)
#     rescue
#       
#       c.to_s
#     end
#   }
# end
Query(Issue)

# Q 2376 : # issue.id
Query(Issue)

# Q 2377 : # issue.status.name
Query(IssueStatus)
.where("id = ?")
.select('name')
# Q 2378 : # issue.status
Query(IssueStatus)
.where("id = ?")
# Q 2379 : # issue.id
Query(Issue)

# Q 2380 : # issue.status.name
Query(IssueStatus)
.where("id = ?")
.select('name')
# Q 2381 : # issue.status
Query(IssueStatus)
.where("id = ?")
# Q 2382 : # issue.id
Query(Issue)

# Q 2383 : # issue.status.name
Query(IssueStatus)
.where("id = ?")
.select('name')
# Q 2384 : # issue.status
Query(IssueStatus)
.where("id = ?")
# Q 2385 : # issue.project.name
Query(Project)
.where("id = ?")
.select('name')
# Q 2386 : # issue.project
Query(Project)
.where("id = ?")
# Q 2387 : # issue.project.name
Query(Project)
.where("id = ?")
.select('name')
# Q 2388 : # issue.project
Query(Project)
.where("id = ?")
# Q 2389 : # issue.project.name
Query(Project)
.where("id = ?")
.select('name')
# Q 2390 : # issue.project
Query(Project)
.where("id = ?")
# Q 2391 : # issue.tracker.name
Query(Tracker)
.where("id = ?")
.select('name')
# Q 2392 : # issue.tracker
Query(Tracker)
.where("id = ?")
# Q 2393 : # issue.tracker.name
Query(Tracker)
.where("id = ?")
.select('name')
# Q 2394 : # issue.tracker
Query(Tracker)
.where("id = ?")
# Q 2395 : # issue.tracker.name
Query(Tracker)
.where("id = ?")
.select('name')
# Q 2396 : # issue.tracker
Query(Tracker)
.where("id = ?")
# Q 2397 : # issue.priority.name
Query(Enumeration)
.where("id = ?")
.select('name')
# Q 2398 : # issue.priority
Query(Enumeration)
.where("id = ?")
# Q 2399 : # issue.priority.name
Query(Enumeration)
.where("id = ?")
.select('name')
# Q 2400 : # issue.priority
Query(Enumeration)
.where("id = ?")
# Q 2401 : # issue.priority.name
Query(Enumeration)
.where("id = ?")
.select('name')
# Q 2402 : # issue.priority
Query(Enumeration)
.where("id = ?")
# Q 2403 : # issue.subject
Query(Issue)
.select('subject')
# Q 2404 : # issue.subject
Query(Issue)
.select('subject')
# Q 2405 : # issue.subject
Query(Issue)
.select('subject')
# Q 2406 : # issue.assigned_to
Query(User)
.where("id = ?")
# Q 2407 : # issue.assigned_to.name
Query(User)
.where("id = ?")
# Q 2408 : # issue.assigned_to
Query(User)
.where("id = ?")
# Q 2409 : # issue.assigned_to
Query(User)
.where("id = ?")
# Q 2410 : # issue.assigned_to.name
Query(User)
.where("id = ?")
# Q 2411 : # issue.assigned_to
Query(User)
.where("id = ?")
# Q 2412 : # issue.assigned_to ? issue.assigned_to.name : ""
Query(Issue)

# Q 2413 : # issue.assigned_to
Query(User)
.where("id = ?")
# Q 2414 : # issue.assigned_to.name
Query(User)
.where("id = ?")
# Q 2415 : # issue.assigned_to
Query(User)
.where("id = ?")
# Q 2416 : # issue.assigned_to ? issue.assigned_to.name : ""
Query(Issue)

# Q 2417 : # issue.author.name
Query(User)
.where("id = ?")
# Q 2418 : # issue.author
Query(User)
.where("id = ?")
# Q 2419 : # issue.author.name
Query(User)
.where("id = ?")
# Q 2420 : # issue.author
Query(User)
.where("id = ?")
# Q 2421 : # issue.author.name
Query(User)
.where("id = ?")
# Q 2422 : # issue.author
Query(User)
.where("id = ?")
# Q 2423 : # issue.start_date
Query(Issue)
.select('start_date')
# Q 2424 : # issue.start_date
Query(Issue)
.select('start_date')
# Q 2425 : # issue.start_date
Query(Issue)
.select('start_date')
# Q 2426 : # issue.start_date
Query(Issue)
.select('start_date')
# Q 2427 : # issue.start_date
Query(Issue)
.select('start_date')
# Q 2428 : # issue.start_date
Query(Issue)
.select('start_date')
# Q 2429 : # issue.due_date
Query(Issue)
.select('due_date')
# Q 2430 : # issue.due_date
Query(Issue)
.select('due_date')
# Q 2431 : # issue.due_date
Query(Issue)
.select('due_date')
# Q 2432 : # issue.due_date
Query(Issue)
.select('due_date')
# Q 2433 : # issue.due_date
Query(Issue)
.select('due_date')
# Q 2434 : # issue.due_date
Query(Issue)
.select('due_date')
# Q 2435 : # Setting.text_formatting
Query(Setting)

# Q 2436 : # issue.done_ratio
Query(Issue)
.select('done_ratio')
# Q 2437 : # issue.done_ratio
Query(Issue)
.select('done_ratio')
# Q 2438 : # issue.done_ratio
Query(Issue)
.select('done_ratio')
# Q 2439 : # issue.created_on
Query(Issue)
.select('created_on')
# Q 2440 : # issue.created_on
Query(Issue)
.select('created_on')
# Q 2441 : # issue.created_on
Query(Issue)
.select('created_on')
# Q 2442 : # issue.updated_on
Query(Issue)
.select('updated_on')
# Q 2443 : # issue.updated_on
Query(Issue)
.select('updated_on')
# Q 2444 : # issue.updated_on
Query(Issue)
.select('updated_on')
# Q 2445 : # @project.all_custom_fields
Query(Project)

# Q 2446 : # issue.custom_value_for(custom_field)
Query(Issue)

# Q 2447 : # issue.custom_value_for
Query(Issue)

# Q 2448 : # issue.custom_value_for(custom_field)
Query(Issue)

# Q 2449 : # issue.custom_value_for
Query(Issue)

# Q 2450 : # issue.custom_value_for(custom_field)
Query(Issue)

# Q 2451 : # issue.custom_value_for
Query(Issue)

# Q 2452 : # issue.custom_value_for(custom_field)
Query(Issue)

# Q 2453 : # issue.custom_value_for
Query(Issue)

# Q 2454 : # issue.custom_value_for(custom_field)
Query(Issue)

# Q 2455 : # issue.custom_value_for
Query(Issue)

# Q 2456 : # Issue.table_name
Query(Issue)

# Q 2457 : # @query.valid?
Query(Query)

# Q 2458 : # @query.statement
Query(Query)

# Q 2459 : # Setting.issues_export_limit.to_i
Query(Setting)

# Q 2460 : # Setting.issues_export_limit
Query(Setting)

# Q 2461 : # IssueStatus.find_by_id(params[:status_id])
Query(IssueStatus)

# Q 2462 : # IssueStatus.find_by_id
Query(IssueStatus)

# Q 2463 : # Enumeration.find_by_id(params[:priority_id])
Query(Enumeration)

# Q 2464 : # Enumeration.find_by_id
Query(Enumeration)

# Q 2465 : # User.find_by_id(params[:assigned_to_id])
Query(User)

# Q 2466 : # User.find_by_id
Query(User)

# Q 2467 : # @project.issue_categories.find_by_id(params[:category_id])
Query(IssueCategory)
.where("project_id = ?")
# Q 2468 : # @project.issue_categories.find_by_id
Query(IssueCategory)
.where("project_id = ?")
# Q 2469 : # @project.issue_categories
Query(IssueCategory)
.where("project_id = ?")
# Q 2470 : # @project.versions.find_by_id(params[:fixed_version_id])
Query(Version)
.where("project_id = ?")
# Q 2471 : # @project.versions.find_by_id
Query(Version)
.where("project_id = ?")
# Q 2472 : # @project.versions
Query(Version)
.where("project_id = ?")
# Q 2473 : # @project.issues.find_all_by_id(params[:issue_ids])
Query(Issue)
.where("project_id = ?")
# Q 2474 : # @project.issues.find_all_by_id(params[:issue_ids])
Query(Issue)
.where("project_id = ?")
# Q 2475 : # @project.issues.find_all_by_id
Query(Issue)
.where("project_id = ?")
# Q 2476 : # @project.issues
Query(Issue)
.where("project_id = ?")
# Q 2477 : # issues.each
Query(Issue)

# Q 2478 : # issue.init_journal(User.current, params[:notes])
Query(Issue)

# Q 2479 : # issue.init_journal(User.current, params[:notes])
Query(Issue)

# Q 2480 : # issue.init_journal
Query(Issue)

# Q 2481 : # User.current
Query(User)

# Q 2482 : # issue.init_journal(User.current, params[:notes])
Query(Issue)

# Q 2483 : # issue.init_journal
Query(Issue)

# Q 2484 : # User.current
Query(User)

# Q 2485 : # issue.status.new_status_allowed_to?(status, current_role, issue.tracker)
Query(IssueStatus)
.where("id = ?")
# Q 2486 : # issue.status.new_status_allowed_to?
Query(IssueStatus)
.where("id = ?")
# Q 2487 : # issue.status
Query(IssueStatus)
.where("id = ?")
# Q 2488 : # issue.tracker
Query(Tracker)
.where("id = ?")
# Q 2489 : # issue.save
Query(Issue)

# Q 2490 : # issue.status.new_status_allowed_to?(status, current_role, issue.tracker)
Query(IssueStatus)
.where("id = ?")
# Q 2491 : # issue.status.new_status_allowed_to?
Query(IssueStatus)
.where("id = ?")
# Q 2492 : # issue.status
Query(IssueStatus)
.where("id = ?")
# Q 2493 : # issue.tracker
Query(Tracker)
.where("id = ?")
# Q 2494 : # issue.save
Query(Issue)

# Q 2495 : # issue.status.new_status_allowed_to?(status, current_role, issue.tracker)
Query(IssueStatus)
.where("id = ?")
# Q 2496 : # issue.status.new_status_allowed_to?
Query(IssueStatus)
.where("id = ?")
# Q 2497 : # issue.status
Query(IssueStatus)
.where("id = ?")
# Q 2498 : # issue.tracker
Query(Tracker)
.where("id = ?")
# Q 2499 : # journal.details.any?
Query(JournalDetail)
.where("journal_id = ?")
# Q 2500 : # journal.details
Query(JournalDetail)
.where("journal_id = ?")
# Q 2501 : # Setting.notified_events.include?("issue_updated")
Query(Setting)

# Q 2502 : # Setting.notified_events.include?
Query(Setting)

# Q 2503 : # Setting.notified_events
Query(Setting)

# Q 2504 : # journal.details.any?
Query(JournalDetail)
.where("journal_id = ?")
# Q 2505 : # journal.details
Query(JournalDetail)
.where("journal_id = ?")
# Q 2506 : # Setting.notified_events.include?("issue_updated")
Query(Setting)

# Q 2507 : # Setting.notified_events.include?
Query(Setting)

# Q 2508 : # Setting.notified_events
Query(Setting)

# Q 2509 : # journal.details.any?
Query(JournalDetail)
.where("journal_id = ?")
# Q 2510 : # journal.details
Query(JournalDetail)
.where("journal_id = ?")
# Q 2511 : # Setting.notified_events.include?("issue_updated")
Query(Setting)

# Q 2512 : # Setting.notified_events.include?
Query(Setting)

# Q 2513 : # Setting.notified_events
Query(Setting)

# Q 2514 : # issue.id
Query(Issue)

# Q 2515 : # issue.id
Query(Issue)

# Q 2516 : # unsaved_issue_ids << issue.id
Query(Issue)

# Q 2517 : # issues.empty?
Query(Issue)

# Q 2518 : # issues.size
Query(Issue)

# Q 2519 : # User.current.allowed_to?(:change_issue_status, @project)
Query(User)

# Q 2520 : # User.current.allowed_to?
Query(User)

# Q 2521 : # User.current
Query(User)

# Q 2522 : # Workflow.find(:all, :include => :new_status, :conditions => { :role_id => current_role.id }).collect(&:new_status).compact.uniq
Query(Workflow)
.where("id = ?")
.where("id != 0")
.distinct('')
# Q 2523 : # Workflow.find(:all, :include => :new_status, :conditions => { :role_id => current_role.id }).collect(&:new_status).compact.uniq
Query(Workflow)
.where("id = ?")
.where("id != 0")
.distinct('')
# Q 2524 : # Workflow.find(:all, :include => :new_status, :conditions => { :role_id => current_role.id }).collect(&:new_status).compact
Query(Workflow)
.where("id = ?")
.where("id != 0")
# Q 2525 : # Workflow.find(:all, :include => :new_status, :conditions => { :role_id => current_role.id }).collect(&:new_status)
Query(Workflow)
.where("id = ?")
# Q 2526 : # Workflow.find(:all, :include => :new_status, :conditions => { :role_id => current_role.id }).collect
Query(Workflow)
.where("id = ?")
# Q 2527 : # Workflow.find(:all, :include => :new_status, :conditions => { :role_id => current_role.id })
Query(Workflow)
.where("id = ?")
# Q 2528 : # Workflow.find
Query(Workflow)
.where("id = ?")
# Q 2529 : # @project.issues.find(params[:issue_ids])
Query(Issue)
.where("project_id = ?")
.where("id = ?")
# Q 2530 : # @project.issues.find(params[:issue_ids])
Query(Issue)
.where("project_id = ?")
.where("id = ?")
# Q 2531 : # @project.issues.find
Query(Issue)
.where("project_id = ?")
.where("id = ?")
# Q 2532 : # @project.issues
Query(Issue)
.where("project_id = ?")
# Q 2533 : # User.current.memberships.each
Query(Member)
.where("user_id = ?")
# Q 2534 : # User.current.memberships
Query(Member)
.where("user_id = ?")
# Q 2535 : # User.current
Query(User)

# Q 2536 : # Tracker.find(:all)
Query(Tracker)
.where("id = ?")
# Q 2537 : # Tracker.find(:all)
Query(Tracker)
.where("id = ?")
# Q 2538 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 2539 : # Project.find_by_id(params[:new_project_id])
Query(Project)

# Q 2540 : # Project.find_by_id(params[:new_project_id])
Query(Project)

# Q 2541 : # Project.find_by_id
Query(Project)

# Q 2542 : # Tracker.find_by_id(params[:new_tracker_id])
Query(Tracker)

# Q 2543 : # Tracker.find_by_id(params[:new_tracker_id])
Query(Tracker)

# Q 2544 : # Tracker.find_by_id
Query(Tracker)

# Q 2545 : # @issues.each
Query(Issue)

# Q 2546 : # News.new(:project => @project)
Query(News)

# Q 2547 : # News.new(:project => @project)
Query(News)

# Q 2548 : # News.new
Query(News)

# Q 2549 : # @news.save
Query(News)

# Q 2550 : # Setting.notified_events.include?("news_added")
Query(Setting)

# Q 2551 : # Setting.notified_events.include?
Query(Setting)

# Q 2552 : # Setting.notified_events
Query(Setting)

# Q 2553 : # @project.id
Query(Project)

# Q 2554 : # News.table_name
Query(News)

# Q 2555 : # @project.name
Query(Project)
.select('name')
# Q 2556 : # @project.name
Query(Project)
.select('name')
# Q 2557 : # @project.versions.find_by_id(params[:version_id])
Query(Version)
.where("project_id = ?")
# Q 2558 : # @project.versions.find_by_id(params[:version_id])
Query(Version)
.where("project_id = ?")
# Q 2559 : # @project.versions.find_by_id
Query(Version)
.where("project_id = ?")
# Q 2560 : # @project.versions
Query(Version)
.where("project_id = ?")
# Q 2561 : # Attachment.create(:container => @version, :file => file, :author => logged_in_user)
Query(Attachment)

# Q 2562 : # Attachment.create(:container => @version, :file => file, :author => logged_in_user)
Query(Attachment)

# Q 2563 : # Attachment.create
Query(Attachment)

# Q 2564 : # @attachments.empty?
Query(Attachment)

# Q 2565 : # Setting.notified_events.include?("file_added")
Query(Setting)

# Q 2566 : # Setting.notified_events.include?
Query(Setting)

# Q 2567 : # Setting.notified_events
Query(Setting)

# Q 2568 : # @project.versions.sort
Query(Version)
.where("project_id = ?")
# Q 2569 : # @project.versions.sort
Query(Version)
.where("project_id = ?")
# Q 2570 : # @project.versions
Query(Version)
.where("project_id = ?")
# Q 2571 : # @project.versions.sort
Query(Version)
.where("project_id = ?")
# Q 2572 : # @project.versions.sort
Query(Version)
.where("project_id = ?")
# Q 2573 : # @project.versions
Query(Version)
.where("project_id = ?")
# Q 2574 : # Tracker.find(:all, :conditions => ["is_in_chlog=?", true], :order => "position")
Query(Tracker)
.where("is_in_chlog = ?")
.where("id = ?")
.where("id = ?")
# Q 2575 : # Tracker.find(:all, :conditions => ["is_in_chlog=?", true], :order => "position")
Query(Tracker)
.where("is_in_chlog = ?")
.where("id = ?")
.where("id = ?")
# Q 2576 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 2577 : # @project.versions.sort
Query(Version)
.where("project_id = ?")
# Q 2578 : # @project.versions.sort
Query(Version)
.where("project_id = ?")
# Q 2579 : # @project.versions
Query(Version)
.where("project_id = ?")
# Q 2580 : # Tracker.find(:all, :conditions => ["is_in_roadmap=?", true], :order => "position")
Query(Tracker)
.where("is_in_roadmap = ?")
.where("id = ?")
.where("id = ?")
# Q 2581 : # Tracker.find(:all, :conditions => ["is_in_roadmap=?", true], :order => "position")
Query(Tracker)
.where("is_in_roadmap = ?")
.where("id = ?")
.where("id = ?")
# Q 2582 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 2583 : # @project.versions.sort
Query(Version)
.where("project_id = ?")
# Q 2584 : # @project.versions.sort
Query(Version)
.where("project_id = ?")
# Q 2585 : # @project.versions
Query(Version)
.where("project_id = ?")
# Q 2586 : # @versions.select
Query(Version)

# Q 2587 : # @project.wiki
Query(Wiki)
.where("id = ?")
# Q 2588 : # @project.repository
Query(Repository)
.where("id = ?")
# Q 2589 : # User.current.allowed_to?("view_#{
# o}".to_sym, @project)
Query(User)

# Q 2590 : # User.current.allowed_to?
Query(User)

# Q 2591 : # User.current
Query(User)

# Q 2592 : # @project.issues.find(:all, :include => [:author, :tracker], :conditions => ["Issue.created_on>=? and Issue.created_on<=?", @date_from, @date_to])
Query(Issue)
.where("project_id = ?")
.where("id = ?")
.where("created_on = ?")
.where("id = ?")
# Q 2593 : # @project.issues.find
Query(Issue)
.where("project_id = ?")
.where("id = ?")
# Q 2594 : # @project.issues
Query(Issue)
.where("project_id = ?")
# Q 2595 : # Issue.table_name
Query(Issue)

# Q 2596 : # Issue.table_name
Query(Issue)

# Q 2597 : # @project.news.find(:all, :conditions => ["News.created_on>=? and News.created_on<=?", @date_from, @date_to], :include => :author)
Query(News)
.where("project_id = ?")
.where("id = ?")
.where("created_on = ?")
.where("id = ?")
# Q 2598 : # @project.news.find
Query(News)
.where("project_id = ?")
.where("id = ?")
# Q 2599 : # @project.news
Query(News)
.where("project_id = ?")
# Q 2600 : # News.table_name
Query(News)

# Q 2601 : # News.table_name
Query(News)

# Q 2602 : # Attachment.find(:all, :select => "Attachment.*", :joins => "LEFT JOIN Version ON Version.id = Attachment.container_id", :conditions => ["Attachment.container_type='Version' and Version.project_id=? and Attachment.created_on>=? and Attachment.created_on<=?", @project.id, @date_from, @date_to], :include => :author)
Query(Attachment)
.where("id = ?")
.where("container_type = ?")
.where("project_id = ?")
.where("created_on = ?")
.where("id = ?")
# Q 2603 : # Attachment.find
Query(Attachment)
.where("id = ?")
# Q 2604 : # Attachment.table_name
Query(Attachment)

# Q 2605 : # Version.table_name
Query(Version)

# Q 2606 : # Version.table_name
Query(Version)

# Q 2607 : # Attachment.table_name
Query(Attachment)

# Q 2608 : # Attachment.table_name
Query(Attachment)

# Q 2609 : # Version.table_name
Query(Version)

# Q 2610 : # Attachment.table_name
Query(Attachment)

# Q 2611 : # Attachment.table_name
Query(Attachment)

# Q 2612 : # @project.id
Query(Project)

# Q 2613 : # @project.documents.find(:all, :conditions => ["Document.created_on>=? and Document.created_on<=?", @date_from, @date_to])
Query(Document)
.where("project_id = ?")
.where("id = ?")
.where("created_on = ?")
.where("id = ?")
# Q 2614 : # @project.documents.find
Query(Document)
.where("project_id = ?")
.where("id = ?")
# Q 2615 : # @project.documents
Query(Document)
.where("project_id = ?")
# Q 2616 : # Document.table_name
Query(Document)

# Q 2617 : # Document.table_name
Query(Document)

# Q 2618 : # Attachment.find(:all, :select => "attachments.*", :joins => "LEFT JOIN Document ON Document.id = Attachment.container_id", :conditions => ["Attachment.container_type='Document' and Document.project_id=? and Attachment.created_on>=? and Attachment.created_on<=?", @project.id, @date_from, @date_to], :include => :author)
Query(Attachment)
.where("id = ?")
.where("container_type = ?")
.where("project_id = ?")
.where("created_on = ?")
.where("id = ?")
# Q 2619 : # Attachment.find
Query(Attachment)
.where("id = ?")
# Q 2620 : # Document.table_name
Query(Document)

# Q 2621 : # Document.table_name
Query(Document)

# Q 2622 : # Attachment.table_name
Query(Attachment)

# Q 2623 : # Attachment.table_name
Query(Attachment)

# Q 2624 : # Document.table_name
Query(Document)

# Q 2625 : # Attachment.table_name
Query(Attachment)

# Q 2626 : # Attachment.table_name
Query(Attachment)

# Q 2627 : # @project.id
Query(Project)

# Q 2628 : # WikiContent.versioned_table_name
Query(WikiContent)

# Q 2629 : # WikiContent.versioned_table_name
Query(WikiContent)

# Q 2630 : # WikiContent.versioned_table_name
Query(WikiContent)

# Q 2631 : # WikiContent.version_column
Query(WikiContent)

# Q 2632 : # WikiPage.table_name
Query(WikiPage)

# Q 2633 : # WikiContent.versioned_table_name
Query(WikiContent)

# Q 2634 : # WikiContent.versioned_table_name
Query(WikiContent)

# Q 2635 : # WikiContent.versioned_table_name
Query(WikiContent)

# Q 2636 : # WikiPage.table_name
Query(WikiPage)

# Q 2637 : # WikiPage.table_name
Query(WikiPage)

# Q 2638 : # WikiContent.versioned_table_name
Query(WikiContent)

# Q 2639 : # Wiki.table_name
Query(Wiki)

# Q 2640 : # Wiki.table_name
Query(Wiki)

# Q 2641 : # WikiPage.table_name
Query(WikiPage)

# Q 2642 : # Wiki.table_name
Query(Wiki)

# Q 2643 : # WikiContent.versioned_table_name
Query(WikiContent)

# Q 2644 : # @project.id
Query(Project)

# Q 2645 : # WikiContent.versioned_class.find(:all, :select => select, :joins => joins, :conditions => conditions)
Query(WikiContent)
.where("id = ?")
# Q 2646 : # WikiContent.versioned_class.find
Query(WikiContent)
.where("id = ?")
# Q 2647 : # WikiContent.versioned_class
Query(WikiContent)

# Q 2648 : # @project.repository.changesets.find(:all, :conditions => ["Changeset.committed_on BETWEEN ? AND ?", @date_from, @date_to])
Query(Changeset)
.where("id = ?")
.where("repository_id = ?")
.where("committed_on = ?")
.where("id = ?")
.where("id = ?")
# Q 2649 : # @project.repository.changesets.find
Query(Changeset)
.where("id = ?")
.where("repository_id = ?")
.where("id = ?")
# Q 2650 : # @project.repository.changesets
Query(Changeset)
.where("id = ?")
.where("repository_id = ?")
# Q 2651 : # @project.repository
Query(Repository)
.where("id = ?")
# Q 2652 : # Changeset.table_name
Query(Changeset)

# Q 2653 : # @project.name
Query(Project)
.select('name')
# Q 2654 : # @project.name
Query(Project)
.select('name')
# Q 2655 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 2656 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 2657 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 2658 : # @project.issues_with_subprojects(params[:with_subprojects])
Query(Project)

# Q 2659 : # @project.issues_with_subprojects
Query(Project)

# Q 2660 : # Issue.find(:all, :include => [:tracker, :status, :assigned_to, :priority, :project], :conditions => ["((start_date BETWEEN ? AND ?) OR (due_date BETWEEN ? AND ?)) AND Issue.tracker_id IN (#{
# @selected_tracker_ids.join(",")})", @calendar.startdt, @calendar.enddt, @calendar.startdt, @calendar.enddt])
Query(Issue)
.where("id = ?")
.where("tracker_id = ?")
.where("start_date = ?")
.where("due_date = ?")
.where("id = ?")
# Q 2661 : # Issue.find
Query(Issue)
.where("id = ?")
# Q 2662 : # Issue.table_name
Query(Issue)

# Q 2663 : # Issue.table_name
Query(Issue)

# Q 2664 : # @project.versions.find(:all, :conditions => ["effective_date BETWEEN ? AND ?", @calendar.startdt, @calendar.enddt])
Query(Version)
.where("project_id = ?")
.where("effective_date = ?")
.where("id = ?")
.where("id = ?")
# Q 2665 : # @project.versions.find
Query(Version)
.where("project_id = ?")
.where("id = ?")
# Q 2666 : # @project.versions
Query(Version)
.where("project_id = ?")
# Q 2667 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 2668 : # Tracker.find(:all, :order => "position")
Query(Tracker)
.where("id = ?")
# Q 2669 : # Tracker.find
Query(Tracker)
.where("id = ?")
# Q 2670 : # User.current.pref
Query(User)

# Q 2671 : # User.current
Query(User)

# Q 2672 : # User.current.pref
Query(User)

# Q 2673 : # User.current
Query(User)

# Q 2674 : # User.current.logged?
Query(User)

# Q 2675 : # User.current
Query(User)

# Q 2676 : # User.current.pref
Query(User)

# Q 2677 : # User.current
Query(User)

# Q 2678 : # User.current.pref
Query(User)

# Q 2679 : # User.current
Query(User)

# Q 2680 : # User.current.pref
Query(User)

# Q 2681 : # User.current
Query(User)

# Q 2682 : # User.current.pref
Query(User)

# Q 2683 : # User.current
Query(User)

# Q 2684 : # User.current.preference.save
Query(UserPreference)
.where("id = ?")
# Q 2685 : # User.current.preference
Query(UserPreference)
.where("id = ?")
# Q 2686 : # User.current
Query(User)

# Q 2687 : # @project.issues_with_subprojects(params[:with_subprojects])
Query(Project)

# Q 2688 : # @project.issues_with_subprojects
Query(Project)

# Q 2689 : # Issue.find(:all, :order => "start_date, due_date", :include => [:tracker, :status, :assigned_to, :priority, :project], :conditions => ["(((start_date>=? and start_date<=?) or (due_date>=? and due_date<=?) or (start_date<? and due_date>?)) and start_date is not null and due_date is not null and Issue.tracker_id in (#{
# @selected_tracker_ids.join(",")}))", @date_from, @date_to, @date_from, @date_to, @date_from, @date_to])
Query(Issue)
.where("id = ?")
.where("start_date = ?")
.where("due_date = ?")
.where("tracker_id = ?")
.where("id = ?")
# Q 2690 : # Issue.find
Query(Issue)
.where("id = ?")
# Q 2691 : # Issue.table_name
Query(Issue)

# Q 2692 : # Issue.table_name
Query(Issue)

# Q 2693 : # @project.versions.find(:all, :conditions => ["effective_date BETWEEN ? AND ?", @date_from, @date_to])
Query(Version)
.where("project_id = ?")
.where("effective_date = ?")
.where("id = ?")
.where("id = ?")
# Q 2694 : # @project.versions.find
Query(Version)
.where("project_id = ?")
.where("id = ?")
# Q 2695 : # @project.versions
Query(Version)
.where("project_id = ?")
# Q 2696 : # @project.identifier
Query(Project)
.select('identifier')
# Q 2697 : # @project.identifier
Query(Project)
.select('identifier')
# Q 2698 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 2699 : # Project.find(params[:id])
Query(Project)
.where("id = ?")
# Q 2700 : # Project.find
Query(Project)
.where("id = ?")
# Q 2701 : # @project.queries.find(params[:query_id])
Query(Query)
.where("project_id = ?")
.where("id = ?")
# Q 2702 : # @project.queries.find(params[:query_id])
Query(Query)
.where("project_id = ?")
.where("id = ?")
# Q 2703 : # @project.queries.find
Query(Query)
.where("project_id = ?")
.where("id = ?")
# Q 2704 : # @project.queries
Query(Query)
.where("project_id = ?")
# Q 2705 : # @project.id
Query(Project)

# Q 2706 : # Query.new(:name => "_", :executed_by => logged_in_user)
Query(Query)

# Q 2707 : # Query.new(:name => "_", :executed_by => logged_in_user)
Query(Query)

# Q 2708 : # Query.new
Query(Query)

# Q 2709 : # @query.add_filter(field, params[:operators][field], params[:values][field])
Query(Query)

# Q 2710 : # @query.add_filter
Query(Query)

# Q 2711 : # @query.add_filter(field, params[:operators][field], params[:values][field])
Query(Query)

# Q 2712 : # @query.available_filters.keys.each
Query(Query)

# Q 2713 : # @query.available_filters.keys
Query(Query)

# Q 2714 : # @query.available_filters
Query(Query)

# Q 2715 : # @query.add_short_filter(field, params[field])
Query(Query)

# Q 2716 : # @query.add_short_filter
Query(Query)

# Q 2717 : # @query.add_short_filter(field, params[field])
Query(Query)

# Q 2718 : # @query.add_short_filter
Query(Query)

# Q 2719 : # Document.new
Query(Document)

# Q 2720 : # Document.new
Query(Document)

# Q 2721 : # Comment.new
Query(Comment)

# Q 2722 : # Comment.new
Query(Comment)

# Q 2723 : # Comment.new
Query(Comment)

# Q 2724 : # Comment.new
Query(Comment)

# Q 2725 : # Comment.new
Query(Comment)

# Q 2726 : # Comment.new
Query(Comment)

# Q 2727 : # Comment.new
Query(Comment)

