#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/proc_fs.h>
#include <linux/seq_file.h>
#include <linux/slab.h>
#include <linux/uaccess.h>

#define PROCFS_NAME "example_rootkit"

static struct proc_dir_entry *proc_file;

static int proc_show(struct seq_file *m, void *v) {
    seq_printf(m, "Hello from rootkit!\n");
    return 0;
}

static int proc_open(struct inode *inode, struct file *file) {
    return single_open(file, proc_show, NULL);
}

static const struct file_operations proc_fops = {
    .owner = THIS_MODULE,
    .open = proc_open,
    .read = seq_read,
    .llseek = seq_lseek,
    .release = single_release,
};

static int __init rootkit_init(void) {
    printk(KERN_INFO "Loading rootkit module...\n");

    proc_file = proc_create(PROCFS_NAME, 0, NULL, &proc_fops);
    if (!proc_file) {
        printk(KERN_ALERT "Error: Could not initialize /proc/%s\n", PROCFS_NAME);
        return -ENOMEM;
    }

    printk(KERN_INFO "/proc/%s created\n", PROCFS_NAME);
    return 0;
}

static void __exit rootkit_exit(void) {
    proc_remove(proc_file);
    printk(KERN_INFO "Unloading rootkit module...\n");
}

module_init(rootkit_init);
module_exit(rootkit_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Hacker");
MODULE_DESCRIPTION("Simple Rootkit Example");
