import java.io.FileInputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Sum {

    public static int sum(FileInputStream fis) throws IOException {
        
	int byteRead;
	// o sum é variável compartilhada.
        int sum = 0;
        
        while ((byteRead = fis.read()) != -1) {
        	sum += byteRead;
        }

        return sum;
    }

    public static long sum(String path) throws IOException {

        Path filePath = Paths.get(path);
        if (Files.isRegularFile(filePath)) {
       	    FileInputStream fis = new FileInputStream(filePath.toString());
            return sum(fis);
        } else {
            throw new RuntimeException("Non-regular file: " + path);
        }
    }


    public static class Task implements Runnable {

	private long sum;
	private String path;

	public Task(String path) {
	    this.path = path;
	}

	@Override
	public void run() {
	    try {
		this.sum = sum(path);
	    } catch (Exception e) {
		e.printStackTrace();
	    }
	}

	public long getSum() {
	    return sum;
	}

    }

    public static void main(String[] args) throws Exception {

        if (args.length < 1) {
            System.err.println("Usage: java Sum filepath1 filepath2 filepathN");
            System.exit(1);
        }

	//many exceptions could be thrown here. we don't care
        for (int i = 0; i < args.length; i++) {
            String path = args[i];
	    Task task = new Task(path);
            Thread t = new Thread(task, "ThreadTask-"+i);
	    t.start();
	    t.join();
	    long sum = task.getSum();
            System.out.println(path + " : " + sum);
        }
    }
}
