# Q 0 : # @context.todos.find_in_state(:all, :active, :order => "todos.due IS NULL, todos.due ASC, todos.created_at ASC")
Query(Todo)
.where("context_id = ?")
# Q 1 : # @user.contexts.find(:all, :include => [:todos])
Query(Context)
.where("user_id = ?")
.where("id = ?")
# Q 2 : # @user.contexts.find(:all, :order => "position ASC")
Query(Context)
.where("user_id = ?")
.where("id = ?")
# Q 3 : # @user.contexts.find(@context_id).not_done_todos.length
Query(Context)
.where("user_id = ?")
.where("id = ?")
# Q 4 : # @user.contexts.find(@item.context_id).not_done_todo_count
Query(Context)
.where("user_id = ?")
.where("id = ?")
# Q 5 : # @user.contexts.find(@item.context_id).todos.count_in_state(:active)
Query(Todo)
.where("user_id = ?")
.where("id = ?")
.where("context_id = ?")
# Q 6 : # @user.contexts.find(@original_item_context_id).not_done_todos.length
Query(Context)
.where("user_id = ?")
.where("id = ?")
# Q 7 : # @user.contexts.find(params["context"])
Query(Context)
.where("user_id = ?")
.where("id = ?")
# Q 8 : # @user.contexts.find(params["context"])
Query(Context)
.where("user_id = ?")
.where("id = ?")
# Q 9 : # @user.contexts.find(params["context"])
Query(Context)
.where("user_id = ?")
.where("id = ?")
# Q 10 : # @user.contexts.find_by_namepart(context)
Query(Context)
.where("user_id = ?")
# Q 11 : # @user.projects.find(:all, :include => [:todos])
Query(Project)
.where("user_id = ?")
.where("id = ?")
# Q 12 : # @user.projects.find(@item.project_id).todos.count_in_state(:active)
Query(Todo)
.where("user_id = ?")
.where("id = ?")
.where("project_id = ?")
# Q 13 : # @user.projects.find(@original_item_project_id).not_done_todos.length
Query(Project)
.where("user_id = ?")
.where("id = ?")
# Q 14 : # @user.projects.find(params["project"])
Query(Project)
.where("user_id = ?")
.where("id = ?")
# Q 15 : # @user.projects.find_by_namepart(project)
Query(Project)
.where("user_id = ?")
# Q 16 : # @user.projects.find_in_state(:all, :active, :order => "position ASC")
Query(Project)
.where("user_id = ?")
# Q 17 : # @user.todos.find(:all, :conditions => ["state = ? or state =?", "active", "completed"])
Query(Todo)
.where("user_id = ?")
.where("id = ?")
.where("state = ?")
.where("id = ?")
# Q 18 : # @user.todos.find(:all, :conditions => ["todos.state = ? or todos.state = ?", "active", "complete"], :include => [:project, :context])
Query(Todo)
.where("user_id = ?")
.where("id = ?")
.where("state = ?")
.where("id = ?")
# Q 19 : # @user.todos.find(:all, :conditions => ["todos.state = ?", "active"], :order => "todos.due IS NULL, todos.due ASC, todos.created_at ASC", :include => [:project, :context])
Query(Todo)
.where("user_id = ?")
.where("state = ?")
.where("id = ?")
.where("id = ?")
# Q 20 : # @user.todos.find(:all, options)
Query(Todo)
.where("user_id = ?")
.where("id = ?")
# Q 21 : # @user.todos.find_in_state(:all, :completed, :order => "completed_at DESC")
Query(Todo)
.where("user_id = ?")
# Q 22 : # @user.todos.find_in_state(:all, :completed, :order => "todos.completed_at DESC")
Query(Todo)
.where("user_id = ?")
# Q 23 : # @user.todos.find_in_state(:all, :deferred, :conditions => ["show_from < ? OR show_from = ?", now, now], :order => "show_from ASC")
Query(Todo)
.where("user_id = ?")
# Q 24 : # @user.todos.find_in_state(:all, :deferred, :order => "show_from ASC")
Query(Todo)
.where("user_id = ?")
# Q 25 : # Context.find(params["context_id"])
Query(Context)
.where("id = ?")
# Q 26 : # Context.find(params[:context][:id])
Query(Context)
.where("id = ?")
# Q 27 : # Context.find_by_id_and_user_id(id, @user.id)
Query(Context)
.where("id = ?")
.where("user_id = ?")
# Q 28 : # Context.find_by_id_and_user_id(params["id"], @user.id)
Query(Context)
.where("id = ?")
.where("user_id = ?")
# Q 29 : # Context.find_by_name_and_user_id(deurlize(params["name"]), @user.id)
Query(Context)
.where("name = ?")
.where("user_id = ?")
# Q 30 : # Project.find(params["project_id"])
Query(Project)
.where("id = ?")
# Q 31 : # Project.find(params[:project][:id])
Query(Project)
.where("id = ?")
# Q 32 : # Project.find_by_id_and_user_id(id, @user.id)
Query(Project)
.where("id = ?")
.where("user_id = ?")
# Q 33 : # Project.find_by_id_and_user_id(params["id"], @user.id)
Query(Project)
.where("id = ?")
.where("user_id = ?")
# Q 34 : # Project.find_by_name_and_user_id(deurlize(params["name"]), @user.id)
Query(Project)
.where("name = ?")
.where("user_id = ?")
# Q 35 : # Todo.count(:conditions => ["todos.#{
# self.class.base_class.name.singularize.downcase}_id = ? AND todos.state = ?", id, "completed"], :order => "completed_at DESC", :include => find_todos_include, :limit => @user.preference.show_number_completed)
Query(Todo)

# Q 36 : # Todo.count(:conditions => ["todos.#{
# self.class.base_class.name.singularize.downcase}_id = ? and #{
# where_state_sql}", id], :order => "todos.due IS NULL, todos.due ASC, todos.created_at ASC", :include => find_todos_include)
Query(Todo)

# Q 37 : # Todo.find(:all, :conditions => ["todos.#{
# self.class.base_class.name.singularize.downcase}_id = ? AND todos.state = ?", id, "completed"], :order => "completed_at DESC", :include => find_todos_include, :limit => @user.preference.show_number_completed)
Query(Todo)
.where("id = ?")
# Q 38 : # Todo.find(:all, :conditions => ["todos.#{
# self.class.base_class.name.singularize.downcase}_id = ? and #{
# where_state_sql}", id], :order => "todos.due IS NULL, todos.due ASC, todos.created_at ASC", :include => find_todos_include)
Query(Todo)
.where("id = ?")
# Q 39 : # Todo.find(:all, :conditions => ["todos.user_id = ? and todos.done = ? and todos.context_id IN (?)", @user.id, false, @item.context_id]).size.to_s
Query(Todo)
.where("id = ?")
.where("user_id = ?")
.where("done = ?")
.where("context_id = ?")
.where("id = ?")
# Q 40 : # Todo.find(:all, :conditions => ["todos.user_id = ? and todos.done = ? and todos.project_id IN (?)", @user.id, false, @item.project_id]).size.to_s
Query(Todo)
.where("id = ?")
.where("user_id = ?")
.where("done = ?")
.where("project_id = ?")
.where("id = ?")
# Q 41 : # Todo.find(:all, :conditions => ["todos.user_id = ? and todos.state = ?", @user.id, "completed"], :order => "todos.completed_at DESC", :limit => max_completed, :include => [:project, :context])
Query(Todo)
.where("id = ?")
.where("user_id = ?")
.where("state = ?")
.where("id = ?")
# Q 42 : # Todo.find(params["id"])
Query(Todo)
.where("id = ?")
# Q 43 : # Todo.find(params["id"])
Query(Todo)
.where("id = ?")
# Q 44 : # Todo.find(params["id"])
Query(Todo)
.where("id = ?")
# Q 45 : # Todo.find(params["id"])
Query(Todo)
.where("id = ?")
# Q 46 : # Todo.find(params["id"].to_i)
Query(Todo)
.where("id = ?")
# Q 47 : # Todo.find_all("done=0 AND context_id=#{
# context.id}").length
Query(Todo)

# Q 48 : # User.find(:first, :conditions => ["is_admin = ?", true])
Query(User)
.where("is_admin = ?")
.where("id = ?")
.where("id = ?")
# Q 49 : # User.find(params["id"])
Query(User)
.where("id = ?")
# Q 50 : # User.find(session["user_id"])
Query(User)
.where("id = ?")
# Q 51 : # find(:first, :conditions => ["login = ?", login])
Query(User)
.where("login = ?")
.where("id = ?")
.where("id = ?")
# Q 52 : # self.find(:all, :conditions => ["done = ? AND context_id = ?", false, id], :order => "due IS NULL, due ASC, created_at ASC")
Query(Todo)
.where("id = ?")
.where("done = ?")
.where("context_id = ?")
.where("id = ?")
# Q 53 : # self.find(:all, :conditions => ["todos.user_id = ? and todos.state = ? and todos.completed_at is not null", user_id, "completed"], :order => "todos.completed_at DESC", :include => [:project, :context])
Query(Todo)
.where("id = ?")
.where("user_id = ?")
.where("state = ?")
.where("completed_at = ?")
.where("id = ?")
